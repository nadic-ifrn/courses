# Modulo 3 - Protocolos de Comunicação de Rede

### Plano do Curso

- [X] Módulo 1 - Introdução aos padrões de comunicação em IoT.
- [X] Módulo 2 - Protocolos de comunicação de dados.
- [X] **Módulo 3 - Protocolos de comunicação de rede**.
- [ ] Módulo 4 - Protocolos de comunicação sem fio.
- [ ] Módulo 5 - Integração de dispositivos e sistemas em soluções IoT.
- [ ] Módulo 6 - Segurança e privacidade em IoT.
- [ ] Módulo 7 - Desenvolvimento de aplicações IoT.

***
### Sobre ao Módulo

Seguindo o nosso curso de _Introdução à Internet das Coisas_ e entramos agora no **Módulo 3**. Só para recapitular, no **Módulo 1** introduzimos o fascinante mundo da IoT, definimos os conceitos básicos e seus principais componentes, suas aplicações, desafios e o impacto significativo que essa tecnologia tem no nosso cotidiano e no futuro que estamos construindo. No **Módulo 2** apresentamos os protocolos de comunicação de dados da camada de aplicação mais usados em IoT, como MQTT, CoAP, HTTP, entre outros. Agora, nesta próxima etapa do nosso curso, _introduziremos os protocolos de comunicação de rede_. Falaremos dos principais tipos de protocolos usados atualmente, como Wi-FI, Ethernet, Redes Móveis (3G, 4G e 5G), LoRaWan. Vamos lá!
***
### Introdução


Como já discutimos em módulos anteriores, um protocolo pode ser entendido como um idioma em que para que ocorra troca de informação é necessário que os dispositivos conectados conheçam a estrutura desse "idioma". Comparando com o inglês, por exemplo, para que duas pessoas se comuniquem é necessário que elas conheçam o vocabulário e a estrutura dessa linguagem (sintaxe). No caso da transmissão de dados em IoT, esses dispositivos que irão enviar e receber dados precisam "conversar na mesma língua", caso contrário os pacotes de mensagens não serão entregues corretamente.


 > Veremos mais adianta que existem diferentes tipos de protocolos, cada um com características particulares de arquitetura, velocidade, distância e taxa de transmissão.

Os protocolos que vimos no módulo 2 estão mais relacionados a camada de aplicação do modelo OSI. Agora, no módulo atual, veremos os protocolos de rede mais utilizados no desenvolvimento de aplicações IoT. Muitos deles vocês já devem ter ouvido falar ou até utilizado, mas agora entederão como é o seu funcionamento e quais sãos suas características principais, de forma que você pode escolher aquele que melhor adeque as necessidades da sua aplicação.

***
#### Ethernet

O protocolo Ethernet (IEEE 802.3) é ainda bastante utilizado hoje em dia apesar de ter sido desenvolvido no final da década de 70. Para que a conexão com a internet ocorra depende de cabos de conexão entre os dispositivos, ou seja, é um protocolo de __conexão com fio__. Entre as principais vantagens estão a alta velocidade de transmissão e o baixo custo. O fato de ser uma conexão que requer cabeamento pode ser uma desvatagens em certas aplicações, principalmente em questão de distância entre os dispositivos conectados a rede.

Na estrutura do modelo OSI, o Ethernet é um protocolo da camada de enlace (camada 2) e é muito utilizado em redes locais (LANs). Este protocolo descreve como os dispositivos se comunicam, enviando e recendos quadros de dados (pacotes), e gerenciam o acesso ao meio físico da comunicação. 

##### 1. Endereçamento MAC

Um importante conceito do protocolo Ethernet é um endereço único que cada dispositivo da rede possui chamado Endereço MAC (Media Access Control). Esse endereço é gravado em hardware é usado para identificar dispositivos na rede e é composto por 48 bits (6 bytes) expressos em notação hexadecimal.


##### 2. Quadros Ethernet

Os dados são transmitidos em quadros Ethernet, que consistem em um cabeçalho, dados e um trailer. No cabeçalho estão contidos informações importantes, como os endereços MAC do remetente e do destinatário e o tipo do dado que está sendo transmitido. Já o trailer é um campo que contém a verificação de redundância cíclica (CRC) para detecção de rede.

##### 3. Controle de Acesso ao Meio

Ethernet utiliza um protocolo de controle de acesso ao meio para gerenciar o acesso de dispositivos à rede compartilhada. No caso da Ethernet tradicional (também chamada de Ethernet com fio), o protocolo é chamado CSMA/CD (Carrier Sense Multiple Access with Collision Detection). Os dispositivos "escutam" o meio para detectar se está ocupado, e se não estiverem, eles podem transmitir dados. Se houver colisões de dados (vários dispositivos transmitindo simultaneamente), o CSMA/CD ajuda a detectar as colisões e atrasa as retransmissões para evitar mais colisões.

##### 4. Tipos

Existem diferentes variantes da Ethernet, cada uma com velocidades e tecnologias de meio físico específicas. Alguns exemplos incluem Ethernet de 10/100/1000/10000 Mbps (10/100/1000/10G Ethernet), bem como Ethernet óptica e Ethernet sem fio (Wi-Fi).


***
#### Wi-Fi

O Wi-Fi, abreviação de "Wireless Fidelity," é uma tecnologia de comunicação sem fio que permite a conectividade de dispositivos em redes locais (LANs) e à internet. Wi-Fi é baseado em uma variedade de padrões definidos pelo IEEE (Institute of Electrical and Electronics Engineers), sendo os mais comuns aqueles que pertencem à família IEEE 802.11.

##### 1. Camadas do Modelo OSI

O Wi-Fi opera em várias camadas do modelo OSI. A camada física (camada 1) lida com a transmissão de sinais sem fio, enquanto a camada de enlace (camada 2) trata de questões como o controle de acesso ao meio e o endereçamento MAC (Media Access Control). As camadas superiores do modelo OSI (camadas de rede, transporte, sessão, apresentação e aplicação) não são especificamente ligadas ao Wi-Fi, mas aplicam-se da mesma forma a redes com e sem fio.

##### 2. Padrões

Existem vários padrões Wi-Fi, como 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, 802.11ax (Wi-Fi 6), e assim por diante. Cada padrão define especificações para a frequência, largura de banda, velocidade de transmissão, segurança e outras características da rede sem fio. Novos padrões são desenvolvidos periodicamente para melhorar o desempenho e a eficiência das redes Wi-Fi.


***
#### Redes Móveis (3G, 4G e 5G)

Os protocolos de redes móveis 3G, 4G e 5G são padrões de comunicação sem fio que definem como os dispositivos móveis se conectam às redes de telefonia celular e à internet. Cada geração representa um avanço tecnológico em termos de velocidade, capacidade, latência e recursos. Veremos cada protocolo em detalhes a seguir.

__3G (Terceira Geração):__ O 3G foi a terceira geração de tecnologia de telefonia móvel e representou uma grande melhoria em relação às redes 2G anteriores, como o GSM. As redes 3G ofereciam velocidades de dados mais rápidas em comparação com o 2G, com taxas de transferência típicas variando de 384 Kbps a 2 Mbps. Além disso, o 3G permitia comunicação de voz e dados simultânea, o que possibilitou serviços como vídeo chamadas e acesso à internet móvel. O Universal Mobile Telecommunications System (UMTS) é um dos padrões 3G mais amplamente utilizados.

__4G (Quarta Geração):__ O 4G representou um grande salto na capacidade de dados e velocidade em comparação com o 3G. Ele permitiu uma experiência de internet móvel mais rápida e confiável. As redes 4G ofereciam velocidades de dados muito mais rápidas, com taxas de transferência típicas variando de 10 Mbps a vários Gbps. Além disso, o 4G reduziu significativamente a latência, o que tornou a comunicação mais responsiva. O Long-Term Evolution (LTE) é um dos padrões 4G mais amplamente utilizados, mas existem várias implementações e variações regionais.

__5G (Quinta Geração):__ O 5G é a mais recente geração de redes móveis, projetada para fornecer velocidades ainda mais rápidas, menor latência e suportar uma variedade de aplicativos e dispositivos inteligentes. O 5G é projetado para oferecer velocidades que variam de centenas de Mbps a vários Gbps, tornando-o substancialmente mais rápido do que o 4G.
Latência: O 5G tem como objetivo uma latência muito baixa, permitindo aplicações críticas em tempo real, como carros autônomos e telesaúde.
Além disso, foi projetado para suportar um grande número de dispositivos conectados simultaneamente, o que é essencial para a Internet das Coisas (IoT). Outra característica do 5G é que ele utiliza uma variedade de frequências, incluindo bandas de ondas milimétricas (mmWave) para alcançar altas velocidades e frequências mais baixas para maior alcance.

#### LoRaWan

O protocolo LoRaWAN (Long Range Wide Area Network) é um protocolo de comunicação de baixo consumo de energia, projetado para redes de área ampla e longo alcance, que suporta comunicação de dispositivos de Internet das Coisas (IoT) em ambientes de baixa potência, como sensores, medidores e rastreadores. 

##### 1. Tecnologia LoRA

LoRa (Long Range) é a tecnologia subjacente do LoRaWAN. Ela utiliza modulação por espalhamento espectral para transmitir dados a longas distâncias (várias dezenas de quilômetros em áreas rurais) com consumo de energia muito baixo.

##### 2. Topologia de Rede

LoRaWAN é projetado para redes de estrela ou de árvore, onde os dispositivos finais (nós) se comunicam com gateways. Os gateways, por sua vez, encaminham os dados para uma rede central.

##### 3. Classes de Dispositivos

O LoRaWAN suporta três classes de dispositivos:

+ __Classe A:__ Dispositivos com comunicação bidirecional, mas com janelas de recepção definidas. Após a transmissão, eles só ouvem as respostas em janelas de tempo específicas.
+ __Classe B:__ Além da comunicação bidirecional, esses dispositivos têm janelas de recepção programadas e adicionam sincronização ao ciclo.
+ __Classe C:__ Esses dispositivos estão sempre prontos para receber dados.

##### 4. Segurança

O LoRaWAN oferece várias camadas de segurança para proteger as comunicações, incluindo criptografia de ponta a ponta, autenticação de dispositivos e chaves de sessão.

##### 5. Banda ISM

O LoRaWAN opera nas faixas ISM (Industrial, Scientific, and Medical) sem licença, o que significa que as frequências estão disponíveis para uso público em muitos países sem a necessidade de licenças adicionais.

##### 6. Baixo Consumo de Energia

O protocolo LoRaWAN é otimizado para dispositivos de baixo consumo de energia. Isso permite que dispositivos alimentados por bateria operem por longos períodos, geralmente vários anos, antes de precisarem de substituição de bateria.

##### 7. Aplicativos IoT Diversos

O LoRaWAN é adequado para uma ampla variedade de aplicações IoT, incluindo monitoramento ambiental, agricultura inteligente, rastreamento de ativos, gerenciamento de estacionamento, monitoramento de qualidade de água, entre outros.
