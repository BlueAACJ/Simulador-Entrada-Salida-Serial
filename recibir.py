import serial, time

def main():
    try:
        # timeout=1 para que readline() expire y podamos reaccionar a Ctrl+C
        with serial.Serial('COM5', 9600, timeout=1) as ser:
            print("📡 Escuchando COM5 (Ctrl+C para salir)...")
            while True:
                # Sólo leemos si hay datos pendientes
                if ser.in_waiting:
                    linea = ser.readline().decode('utf-8', errors='ignore').strip()
                    if linea: 
                        print(f"Recibido: {linea}")
                else:
                    # evita 100% CPU cuando no hay nada
                    time.sleep(0.1)

    except KeyboardInterrupt:
        print("\n👋 Interrupción de teclado detectada. Cerrando puerto…")
    except Exception as e:
        print(f"❌ Error en serial: {e!r}")

if __name__ == "__main__":
    main()
