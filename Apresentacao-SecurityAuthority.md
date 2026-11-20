# Sistema SecurityAuthority para Roblox

## Objetivo

Este módulo concentra a validação de segurança no servidor para um jogo Roblox. Ele monitora jogadores, valida ações remotas, bloqueia estados inválidos e aplica isolamento persistente por `UserId`.

O código não deve receber decisões de dano, recompensa ou movimento vindas do cliente. Todas as consequências relevantes continuam sendo calculadas no servidor.

## Arquitetura

O `SecurityAuthority` funciona como um ModuleScript localizado em `ServerScriptService`.

Ele mantém um estado autoritativo por jogador com:

- suspeita acumulada e decaimento;
- estado de quarentena;
- estado de movimento;
- estado de agarrão;
- grace para teleportes e liberações legítimas;
- histórico curto de eventos;
- limite de remotes;
- cooldown de ataque e ações;
- teleporte pendente;
- locks de ações concorrentes.

O módulo cria ou reutiliza a pasta `ReplicatedStorage.SecurityRemotes` e registra os seguintes remotes:

- `PerformAction`;
- `AttemptGrabEscape`;
- `PerformAttack`.

## Funcionalidades principais

- Inicialização automática dos jogadores presentes e futuros.
- Limpeza do estado em `PlayerRemoving`.
- Monitoramento periódico em `RunService.Heartbeat`.
- Quarentena contínua e persistente por `UserId`.
- Remoção de ferramentas e animações durante isolamento.
- Validação de payload por allowlist.
- Bloqueio de campos e tipos inválidos.
- Validação de Vetores3 contra NaN, infinito e magnitude excessiva.
- Limite de frequência de remotes.
- Cooldown independente para ataques e ações.
- Validação de alvo aliado, área de combate, distância e linha de visão.
- Dano autoritativo configurado em `AttackDamage`, atualmente com valor 10.
- Handlers servidor-side para:
  - `UseODM`;
  - `DodgeDash`;
  - `InteractObject`.
- Controle server-side de início e fim de agarrões.
- Decaimento de suspeita ao longo do tempo.
- Registro crítico no DataStore.
- Hooks de teste para relógio e Raycast.

## Integração

O módulo pode ser carregado em um Script do `ServerScriptService`:

```lua
local SecurityAuthority = require(script.Parent:WaitForChild("SecurityAuthority"))

-- Integração opcional
SecurityAuthority.SetAttackHandler(function(player, targetModel)
	-- Executar efeitos específicos do jogo, animações ou validações complementares.
end)

SecurityAuthority.SetActionHandler("MinhaAcao", function(player, payload)
	-- Implementar apenas consequências calculadas no servidor.
	return true
end)

SecurityAuthority.StartServerIntegration()
```

`StartServerIntegration` já é chamado pelo próprio módulo. Isso permite usar o sistema sem bootstrap externo, mas integrações específicas do jogo ainda devem ser instaladas antes de expor o RemoteEvent ao cliente.

## Estados de movimento

Os estados suportados são:

- `normal`;
- `vehicle`;
- `grabbed`;
- `knockback`;
- `respawn`.

Teleportes legítimos devem ser registrados pelo servidor por `RegisterServerTeleport`. Agarrões legítimos devem usar `BeginGrab` e `EndGrabLegitimately`.

## Quarentena

`IsolatePlayer` marca o jogador como isolado e persiste o registro no DataStore `SecurityQuarantine_v1`.

O monitor continua aplicando as restrições no servidor. `ReleaseQuarantine` remove o estado em memória e a persistência, mas deve ser exposto somente a código administrativo autorizado.

## O que o cliente pode enviar

O cliente deve enviar apenas intenção e dados essenciais, como:

- nome da ação;
- alvo de ataque;
- direção ou ponto de engate;
- identificação do objeto interagível;
- origem pública de um agarrão.

O cliente não deve enviar:

- dano;
- recompensa;
- distância;
- velocidade;
- estado de equipe;
- teleporte;
- resultado de validação;
- valor de linha de visão.

## Pontos para revisão pelo desenvolvedor Roblox

1. Confirmar que todos os remotes sensíveis existentes passam pelo módulo.
2. Substituir ou complementar os handlers padrão conforme as mecânicas reais do jogo.
3. Configurar `CombatZone` e `QuarantineZone` no Workspace.
4. Definir dano, distância, cooldown e animações de acordo com cada personagem.
5. Adicionar marcação `TargetId` nos objetos permitidos para interação.
6. Marcar interfaces e prompts sensíveis com `RestrictInQuarantine = true`, quando necessário.
7. Executar testes em Studio com latência simulada.
8. Validar veículos, knockback, lag, agarrões e respawns antes de ativar penalidades.
9. Manter `EnableAutoKick` desativado até calibrar os thresholds.
10. Confirmar que o DataStore está habilitado e monitorado no ambiente publicado.

## Cenários de teste recomendados

- Jogador normal se move dentro dos limites.
- Jogador atravessa o mapa por teleporte legítimo.
- Jogador entra e sai de veículo.
- Knockback legítimo excede temporariamente o limite.
- Jogador é agarrado e liberado pelo servidor.
- Cliente envia escape rápido ou origem divergente.
- Cliente chama o mesmo remote em alta frequência.
- Payload contém campos extras, tipos errados, NaN ou infinito.
- Ataque sem linha de visão.
- Ataque fora de alcance.
- Ataque contra aliado.
- Ataque durante respawn ou agarrão.
- Reentrada de jogador que possui quarentena persistente.
- Aplicação de dano contra humanoide já morto.
- Falha temporária do DataStore.

## Riscos conhecidos

- A movimentação ainda pode gerar falsos positivos em mecânicas físicas complexas.
- O Raio de interação entre personagem e objeto depende da geometria real da experiência.
- A persistência da quarentena precisa de tratamento de falhas do DataStore.
- Handlers específicos do jogo ainda devem ser definidos conforme a mecânica de cada personagem.
- `EnableAutoKick = false` mantém a quarentena em vez da expulsão.

## Configuração atual

Valores relevantes no bloco `Config`:

- limiar de suspeita: 10;
- dano autoritativo: 10;
- limite de ataque: 18 studs;
- cooldown de ataque: 0.35 segundos;
- decaimento de suspeita: 0.25 por segundo;
- limite de chamadas remotas: 15 por segundo;
- auto kick: desativado;
- DataStore crítico: ativado;
- quarentena persistente: ativada;
- linha de visão: requerida.
