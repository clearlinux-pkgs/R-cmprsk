#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-cmprsk
Version  : 2.2.10
Release  : 27
URL      : https://cran.r-project.org/src/contrib/cmprsk_2.2-10.tar.gz
Source0  : https://cran.r-project.org/src/contrib/cmprsk_2.2-10.tar.gz
Summary  : Subdistribution Analysis of Competing Risks
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-cmprsk-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
subdistribution functions in competing risks, as described in Gray
 (1988), A class of K-sample tests for comparing the cumulative

%package lib
Summary: lib components for the R-cmprsk package.
Group: Libraries

%description lib
lib components for the R-cmprsk package.


%prep
%setup -q -c -n cmprsk
cd %{_builddir}/cmprsk

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1591716849

%install
export SOURCE_DATE_EPOCH=1591716849
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cmprsk
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cmprsk
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cmprsk
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc cmprsk || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/cmprsk/DESCRIPTION
/usr/lib64/R/library/cmprsk/INDEX
/usr/lib64/R/library/cmprsk/Meta/Rd.rds
/usr/lib64/R/library/cmprsk/Meta/features.rds
/usr/lib64/R/library/cmprsk/Meta/hsearch.rds
/usr/lib64/R/library/cmprsk/Meta/links.rds
/usr/lib64/R/library/cmprsk/Meta/nsInfo.rds
/usr/lib64/R/library/cmprsk/Meta/package.rds
/usr/lib64/R/library/cmprsk/NAMESPACE
/usr/lib64/R/library/cmprsk/R/cmprsk
/usr/lib64/R/library/cmprsk/R/cmprsk.rdb
/usr/lib64/R/library/cmprsk/R/cmprsk.rdx
/usr/lib64/R/library/cmprsk/help/AnIndex
/usr/lib64/R/library/cmprsk/help/aliases.rds
/usr/lib64/R/library/cmprsk/help/cmprsk.rdb
/usr/lib64/R/library/cmprsk/help/cmprsk.rdx
/usr/lib64/R/library/cmprsk/help/paths.rds
/usr/lib64/R/library/cmprsk/html/00Index.html
/usr/lib64/R/library/cmprsk/html/R.css
/usr/lib64/R/library/cmprsk/tests/Rplots.pdf
/usr/lib64/R/library/cmprsk/tests/Rplots.ps
/usr/lib64/R/library/cmprsk/tests/test.R
/usr/lib64/R/library/cmprsk/tests/test.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/cmprsk/libs/cmprsk.so
/usr/lib64/R/library/cmprsk/libs/cmprsk.so.avx2
/usr/lib64/R/library/cmprsk/libs/cmprsk.so.avx512
