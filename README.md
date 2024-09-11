# Free-Streaming

<div align="center">
  <a href="https://github.com/osthread/">
    <img src="og_trinix.png" alt="Logo" width="150" height="80">
  </a>

  <h3 align="center">Trinix Free-Streaming</h3>

  <p align="center">
    Your go-to free streaming service, making entertainment accessible for everyone.
    <br/>
  </p>
</div>

## About The Project

Trinix is a free streaming service designed to make entertainment accessible for everyone. Paired with the Trinix Discord bot, you can effortlessly search and enjoy the latest trending movies and TV shows. With its automatic update feature, your channel stays in sync with the freshest content.

**Note:** The creators of Trinix are not responsible for any actions taken by users of this service.

### Built With

* Python 3.9

## Getting Started

Follow these simple steps to get Trinix up and running on your local machine.

### Prerequisites

Ensure you have Python 3.9 installed before proceeding.

### Installation

1. Install required Python packages:
   ```sh
   pip install flask flask-cors waitress
   ```

2. Install Node.js and npm:
   ```sh
   apt install nodejs npm
   ```

3. Install PM2 globally:
   ```sh
   npm install pm2@latest -g
   ```

## Usage

To start the Trinix server:

```sh
pm2 start main.py --interpreter python3
```

Other useful PM2 commands:

```sh
pm2 list                # List all processes
pm2 restart <ID>        # Restart a process
pm2 stop <ID>           # Stop a process
```

## License

Distributed under the GPL-3.0 License. See `LICENSE.txt` for more information.

## Acknowledgments
* Logo by gh0st_artz
