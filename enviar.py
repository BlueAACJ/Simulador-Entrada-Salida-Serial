import serial, time, random
from datetime import datetime

# Lista de productos y códigos
productos = [
    "Cerdo entero","Carne de res","Pollo entero","Carne molida de res",
    "Costillas de cerdo","Lomo de cerdo","Filete de res","Pierna de cerdo",
    "Alitas de pollo","Pechuga de pollo"
]
codigos = {p: random.randint(100000, 999999) for p in productos}

def main():
    try:
        # timeout=1 asegura que write() no quede colgado
        with serial.Serial('COM6', 9600, timeout=1) as ser:
            print("✅ Puerto serial abierto en COM6")
            print("🔄 Enviando datos (Ctrl+C para parar)...")
            while True:
                producto = random.choice(productos)
                codigo   = codigos[producto]
                peso     = round(random.uniform(10,100),2)
                fecha    = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                msg      = f"{producto}, {codigo}, {peso}, {fecha}\n"
                
                ser.write(msg.encode('utf-8'))
                print(msg.strip())
                # Cada 5 seg 
                time.sleep(5)

    except KeyboardInterrupt:
        print("\n🚩 Simulación interrumpida por el usuario.")
    except Exception as e:
        print(f"❌ Error inesperado: {e!r}")

if __name__ == "__main__":
    main()
