%define		pkgname	news
Summary:	The News app is a an RSS/Atom feed aggregator.
Name:		owncloud-%{pkgname}
Version:	1.401
Release:	1
License:	AGPL
Group:		Development/Languages/PHP
Source0:	http://apps.owncloud.com/CONTENT/content-files/158434-news.zip
# Source0-md5:	4df61a12be48770f6bec663927df2360
URL:		http://apps.owncloud.com/content/show.php/News?content=158434
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	owncloud >= 5.0.6
Requires:	owncloud-appframework >= 0.102
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/owncloud/apps/%{pkgname}

%description
The News app is a an RSS/Atom feed aggregator.

%prep
%setup -q -n %{pkgname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}

cp -a * $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
