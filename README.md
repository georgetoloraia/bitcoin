# Bitcoin: A Python-Based Blockchain Implementation

## Abstract

This project is a Python-based blockchain system that introduces a novel Proof-of-Work mechanism using elliptic curve scalar multiplication. It emphasizes energy efficiency, decentralization, and robust cryptographic security.

## Features

- **Blockchain Core**: Implements a scalable and secure blockchain architecture.
- **Scalar Multiplication Mining**: Utilizes elliptic curve cryptography for block validation.
- **P2P Networking**: Facilitates decentralized peer-to-peer communication.
- **Configurable CLI**: Allows interaction with the blockchain through a command-line interface.

## Download and Run the Bitcoin Node

### Step 1: Download the Executable
- Go to the [Releases page](https://github.com/<username>/<repo>/releases).
- Download the appropriate file for your system:
  - For Windows: `main.exe`
  - For Linux/macOS: `main`

### Step 2: Run the Executable
1. Open a terminal (or command prompt on Windows).
2. Navigate to the folder where you downloaded the executable.
3. Run the program:
   - On Linux/macOS:
     ```bash
     ./main
     ```
   - On Windows:
     ```
     main.exe
     ```

### Step 3: Interact with the Node
Follow the on-screen instructions to start your Bitcoin node and interact with it!


## Project Structure

```bash
bitcoin/
├── core/
│   ├── blockchain.py       # Blockchain and block classes
│   ├── transaction.py      # Transaction and wallet classes
│   ├── mining.py           # Mining algorithms and utilities
│   ├── keys.py             # Cryptographic key handling
│
├── network/
│   ├── p2p.py              # P2P communication and node handling
│   ├── protocol.py         # Message handling and propagation
│
├── utils/
│   ├── crypto.py           # Cryptographic utilities
│   ├── db.py               # Persistent storage handling
│   ├── helpers.py          # Miscellaneous helper functions
│
├── tests/                  # Unit tests for various modules
│
├── main.py                 # Main entry point for starting the node
├── cli.py                  # Command-line interface for blockchain interaction
├── config.py               # Configuration settings
├── setup.py                # Project setup script
├── requirements.txt        # Dependencies list
└── README.md               # Project documentation
```

---

## Installation

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package manager)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/georgetoloraia/bitcoin.git
   cd bitcoin
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install the project locally:
   ```bash
   python setup.py install
   ```

---

## Usage

### Start the Node

Run the `main.py` script to start the node:
```bash
python main.py --host 127.0.0.1 --port 8333
```
By default, the node listens on `127.0.0.1:8333`.

### Interact with the CLI

The `cli.py` script allows interaction with the blockchain:
```bash
python cli.py
```

#### Available Commands
- `mine_block`: Initiates the mining process.
- `add_transaction`: Adds a transaction to the mempool.
- `show_blockchain`: Displays the current state of the blockchain.

### Run Tests

To ensure the project is functioning correctly, run the test suite:
```bash
pytest tests/
```

---

## How It Works

### Blockchain Core
- Maintains a chain of blocks with validated transactions.
- Supports dynamic difficulty adjustment for mining.

### Mining
- Utilizes elliptic curve scalar multiplication instead of traditional hashing.
- Reduces energy consumption while maintaining security.

### P2P Networking
- Nodes communicate using a custom protocol to propagate transactions and blocks.

---

## How to Contribute

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## Contact

- **Author**: George Toloraia  
- **Email**: georgetoloraia@gmail.com  
- **GitHub**: [georgetoloraia](https://github.com/georgetoloraia)

