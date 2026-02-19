echo "Installing Python......"
pkg install python -y > /dev/null 2>&1
echo "Installing php......"
pkg install php -y > /dev/null 2>&1
echo "Installing Cloudflared......"
pkg install cloudflared -y > /dev/null 2>&1
pip install termcolor > /dev/null 2>&1

sleep 1

mkdir JSON

mv /data/data/com.termux/files/home/DGTL-BGMI/index.php JSON

mv /data/data/com.termux/files/home/DGTL-BGMI/result.php JSON

mv /data/data/com.termux/files/home/DGTL-BGMI/setup.sh JSON

mv /data/data/com.termux/files/home/DGTL-BGMI/Dgtlbgmi.py JSON

bash run.sh