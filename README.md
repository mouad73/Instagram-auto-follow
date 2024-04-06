# Instagram Automation Script

This repository contains a Python script for automating follow actions on Instagram using Selenium. The script is designed to help grow your Instagram audience by following users in your target audience.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.
- Install the required Python packages using the following command:

pip install -r requirements.txt

- Google Chrome browser installed.
- ChromeDriver compatible with your Chrome version. You can use `webdriver_manager` to automatically download the correct version.

### Installation

1. Clone this repository to your local machine:
git clone https://github.com/mouad73/instagram-auto-follow.git

2. Navigate to the project directory:
cd instagram-automation-script
3. Install the required Python packages:
pip install -r requirements.txt

### Usage

1. Modify the `config.yaml` file with your Instagram credentials, hashtags, and other settings.
2. Run the script using the command:
python instagram_auto_follow.py


### Automation

To automate the script using Task Scheduler (Windows) or cron jobs (Linux/macOS), follow the instructions provided in the `automation_guide.md` file.

## File Structure

- `instagram_auto_follow.py`: The main Python script for automating Instagram follows.
- `config.yaml`: Configuration file for storing Instagram credentials and settings.
- `automation_guide.md`: Guide for automating the script using Task Scheduler (Windows) or cron jobs (Linux/macOS).
- `run_instagram_script.bat`: Batch file for running the script on Windows.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
