%define		pkgname	news
Summary:	The News app is a an RSS/Atom feed aggregator.
Name:		owncloud-%{pkgname}
Version:	1.001
Release:	0.1
License:	AGPL
Group:		Development/Languages/PHP
Source0:	http://apps.owncloud.com/CONTENT/content-files/158434-news.zip
# Source0-md5:	f9a77ddf834e038f0fc4541af4929bfd
URL:		http://apps.owncloud.com/content/show.php/News?content=158434
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	owncloud >= 5.0.0
Requires:	owncloud-appframework >= 0.101
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/owncloud/%{pkgname}

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
