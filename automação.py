import requests
from urllib.parse import urljoin

# Lista de diretórios e arquivos sensíveis mais comuns em auditorias
DIRECTORIES = [
    "admin/",
    "administrator/",
    "login/",
    "wp-admin/",
    "backup/",
    "config.json",
    ".env",
    "robots.txt"
]

# Cabeçalhos de segurança essenciais recomendados pela OWASP
SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security"
]

def scan_target(target_url):
    print(f"\n[+] Iniciando varredura de segurança em: {target_url}\n")
    
    # Normaliza a URL garantindo que comece com http://
    if not target_url.startswith("http"):
        target_url = "http://" + target_url
        
    # Headers simulando um navegador real para evitar bloqueios automáticos (WAF básico)
    headers_requisicao = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) SecurityAuditor/1.0"
    }
        
    # ==========================================
    # PARTE 1: Verificação de Cabeçalhos de Segurança
    # ==========================================
    print("--- [ 1 ] Verificando Cabeçalhos de Segurança HTTP ---")
    try:
        # Faz uma requisição GET para a página principal com limite de 5 segundos de espera
        response = requests.get(target_url, headers=headers_requisicao, timeout=5)
        headers_recebidos = response.headers
        
        for header in SECURITY_HEADERS:
            if header in headers_recebidos:
                print(f"   [PRESENTE] {header}")
            else:
                print(f"   [AUSENTE]  {header} (Recomendado implementar)")
                
    except requests.exceptions.RequestException as e:
        print(f"[-] Erro crítico ao acessar o site principal: {e}")
        return

    # ==========================================
    # PARTE 2: Varredura de Diretórios e Arquivos Expostos
    # ==========================================
    print("\n--- [ 2 ] Verificando Diretórios e Arquivos Sensíveis ---")
    encontrados = 0
    
    for directory in DIRECTORIES:
        # urljoin junta a URL base com o diretório atual de forma segura
        full_url = urljoin(target_url, directory)
        try:
            # timeout menor (3s) para agilizar a varredura
            res = requests.get(full_url, headers=headers_requisicao, timeout=3)
            
            # Status 200 (OK) significa que a página abriu livremente
            if res.status_code == 200:
                print(f"   [ENCONTRADO (200 OK)] {full_url}")
                encontrados += 1
            # Status 403 (Forbidden) significa que o arquivo/diretório existe, mas está protegido
            elif res.status_code == 403:
                print(f"   [PROTEGIDO/403]   {full_url}")
                encontrados += 1
                
        except requests.exceptions.RequestException:
            # Ignora erros de conexão pontuais em diretórios que não existem
            pass

    print(f"\n[+] Varredura concluída! Total de caminhos detectados: {encontrados}")

if __name__ == "__main__":
    url_alvo = input("Digite a URL alvo (ex: meudominio.com ou http://testphp.vulnweb.com): ")
    scan_target(url_alvo)
