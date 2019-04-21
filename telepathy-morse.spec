%define date 20190421

Name:       telepathy-morse
Summary:    A Telegram connection manager
Version:    0.2.0
Release:    1.%{date}.0
Group:      Applications/Communications
License:    GPLv2+
URL:        https://github.com/TelepathyIM/telepathy-morse
Source0:    telepathy-morse-%{version}-%{date}.tar.xz
BuildRequires: pkgconfig(dbus-1) >= 1.1.0
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(TelegramQt5) >= 0.2.0
BuildRequires: pkgconfig(TelepathyQt5) >= 0.9.6
BuildRequires: pkgconfig(TelepathyQt5Service) >= 0.9.6
BuildRequires: pkgconfig(TelepathyQt5Farstream) >= 0.9.6
BuildRequires: cmake >= 2.8

%description
A Telegram connection manager.

%prep
%setup -q -n %{name}-%{version}-%{date}

%build
%cmake
%make_build

%install
%make_install -C build

%files
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager
