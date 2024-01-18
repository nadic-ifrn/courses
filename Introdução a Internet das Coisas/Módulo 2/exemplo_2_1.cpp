// a função setup é executada apenas uma vez quando você pressiona o reset ou liga a placa
void setup() {
    // inicializa o pino digital chamado LED_BUILTIN como uma saída
    pinMode(LED_BUILTIN, OUTPUT);
}

// a função loop roda para sempre
void loop() {
    // Aciona a pino do LED colocando em nível “alto”
    digitalWrite(LED_BUILTIN, HIGH);
    delay(1000); // espera por um segundo
    digitalWrite(LED_BUILTIN, LOW); 
    // Coloca o pin em nível baixo    
    delay(1000); // espera por um segundo
}