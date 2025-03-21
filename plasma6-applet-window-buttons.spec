Name:		plasma6-applet-window-buttons
Version:	0.14.0
Release:	1
Source0:	https://github.com/moodyhunter/applet-window-buttons6/archive/refs/tags/v%{version}.tar.gz
Summary:	Plasma applet to show window buttons in panels
URL:		https://github.com/moodyhunter/applet-window-buttons6
License:	GPL
Group:		Graphical desktop/KDE
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KDecoration3)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6Package)
BuildRequires:	cmake(KF6Svg)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Qml)
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
This is a Plasma 6 applet that shows the current window appmenu in
one's panels. This plasmoid is coming from Latte land, but it can also
support Plasma panels.

%files
%{_qtdir}/qml/org/kde/appletdecoration
%{_datadir}/metainfo/org.kde.windowbuttons.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.windowbuttons
