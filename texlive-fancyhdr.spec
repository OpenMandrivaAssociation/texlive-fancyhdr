Name:		texlive-fancyhdr
Version:	72910
Release:	1
Summary:	Extensive control of page headers and footers in LaTeX2e
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fancyhdr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyhdr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancyhdr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides extensive facilities, both for
constructing headers and footers, and for controlling their use
(for example, at times when LaTeX would automatically change
the heading style in use).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fancyhdr
%doc %{_texmfdistdir}/doc/latex/fancyhdr

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
