%define version 2023.03.18
%define bindir /home/ze/development/clash-premium-rpmbuild/bin

Summary: Clash Premium RPM Package
Name: clash-premium
Version: %{version}
Release: 1
License: non-free
URL: https://github.com/Dreamacro/clash/releases/tag/premium
Group: System
Packager: Phang Cheung

%description
A rule-based tunnel in Go. 

%post
sudo sh -c 'echo -e "[Unit]\nDescription=A rule based proxy tunnel\nAfter=network-online.target\n\n[Service]\nType=simple\nRestart=on-aboard\nExecStart=/usr/bin/clash -d /etc/clash\n\n[Install]\nWantedBy=default.target" > /etc/systemd/system/clash.service'
sudo systemctl --system enable clash.service

%postun
sudo systemctl disable clash.service
sudo rm /etc/systemd/system/clash.service

%prep
mkdir -p $RPM_BUILD_ROOT/usr/bin # We write to /usr/bin since we are package now.
cp %{bindir}/clash-linux-amd64-v3 $RPM_BUILD_ROOT/usr/bin/clash
exit

%files
%attr(0755, root, root) /usr/bin/clash

%changelog
Update clash premium version to 2023.03.18
