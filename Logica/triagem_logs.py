logs_brutos = [ "2024-07-15 08:42:17 | ERROR | auth-service | ip=192.168.4.21 | Login failed: invalid credentials",     
                "2024-07-15 08:43:02 | INFO  | api-gateway  | ip=10.0.0.5     | Request completed: 200 OK",     
                "2024-07-15 08:43:45 | WARN  | db-connector | ip=10.0.1.12    | Connection pool at 87% capacity",     
                "2024-07-15 08:44:10 | ERROR | auth-service | ip=192.168.4.21 | Login failed: invalid credentials",     
                "2024-07-15 08:46:30 | CRITICAL | firewall  | ip=192.168.4.21 | Port scan detected: 1024 ports/5s"]

for linha in logs_brutos:
    if"ERROR" in linha or "CRITICAL" in linha:
        partes = [p.strip() for p in linha.t("|")]
        nivel = partes[1]
        servico = partes[2]
        ip = ""
        for parte in partes:
            if parte.starswit("ip="):
                ip = parte.replace("ip=","")
                break
            mensagem = "|".join(partes[3]:)
            print(f"ALERTA DE SEGURANÇA! Nível:[{nivel}] | Origem:[{ip}]
            Menssagem: [{serviço}] {mensagem}")

        