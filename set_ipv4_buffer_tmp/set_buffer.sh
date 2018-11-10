cat /proc/sys/net/ipv4/tcp_rmem
cat /proc/sys/net/ipv4/tcp_wmem

sudo sysctl -w net.ipv4.tcp_rmem='5000000 10000000 10000000'
sudo sysctl -w net.ipv4.tcp_wmem='5000000 10000000 10000000'

cat /proc/sys/net/ipv4/tcp_rmem
cat /proc/sys/net/ipv4/tcp_wmem

sudo sysctl -w net.ipv4.route.flush=1
