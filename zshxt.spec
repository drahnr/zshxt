Name:           zshxt
Version:        0.0.2
Release:        1%{?dist}
Summary:        A fork of oh-my-zsh

License:        MIT
URL:            https://ahoi.io/zshxt
Source0:        %{name}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:		noarch
Requires:		zsh


%description
A fork of oh-my-zsh which deals with global setup.

%prep
%setup -q -n %{name}


%build


%install
pwd
rm -rf $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT
install -m0755 -d ${DESTDIR}%{_datadir}/%{name}
cp -Rf zshxt.sh lib plugins templates themes ${DESTDIR}%{_datadir}/%{name}/
chmod 0755 -Rf ${DESTDIR}%{_datadir}/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
#%doc README.md
%{_datadir}/%{name}/*


%changelog
* Sun Mar 27 2016  Bernhard Schuster  <bernhard@ahoi.io> 0.0.1
- Initial version
