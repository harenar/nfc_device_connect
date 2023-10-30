import nfc

def read_nfc_card(device):
    while True:
        print("Please scan your card...")
        target = device.poll(0.5)
        if target:
            id = target.identifier
            print("Card Detected! ID: ", id)
            return id

def main():
    try:
        with nfc.ContactlessFrontend('usb') as clf:
            clf.connect(rdwr={'on-connect': read_nfc_card})
    except nfc.CLFError as error:
        print(f"An error occurred while connecting to the NFC device: {error}")

if __name__ == "__main__":
    main()