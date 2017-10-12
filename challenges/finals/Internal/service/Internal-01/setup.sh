apt update && apt upgrade -y && apt install net-tools openssh-server
cat > /etc/ssh/sshd_config << EOL
Port 9909
AddressFamily inet
SyslogFacility AUTH
LogLevel INFO
Protocol 2
HostKey /etc/ssh/ssh_host_ed25519_key
LoginGraceTime 15
PermitRootLogin no
StrictModes yes
PubkeyAuthentication no
HostbasedAuthentication no
IgnoreUserKnownHosts yes
IgnoreRhosts yes
PasswordAuthentication yes
PermitEmptyPasswords no
ChallengeResponseAuthentication no
UsePAM yes
AllowAgentForwarding no
AllowStreamLocalForwarding no
AllowTcpForwarding no
GatewayPorts no
X11Forwarding no
TCPKeepAlive no
UsePrivilegeSeparation yes
ClientAliveInterval 60
ClientAliveCountMax 3
DebianBanner no
PrintMotd no
AcceptEnv LANG LC_*
Subsystem sftp internal-sftp
Match Group sftponly
    ChrootDirectory %h
    ForceCommand internal-sftp
    AllowTcpForwarding no
EOL
groupadd sftponly
useradd deathline -g sftponly -s /bin/false -d /flag
useradd -r -s /bin/false void
useradd -r -s /bin/false duck
useradd -r -s /bin/false exetr
useradd -r -s /bin/false kkkkk
service ssh restart
ifconfig
