################################################################################
### BLAS and LAPACK
### Raynaud 2006
################################################################################
AC_DEFUN([AC_SR_SPANLIB_DOC],[

	# docbook (xslt) processor support
	AS_DOCBOOK(:,AS_VAR_SET(XSLTPROC))

	# We need perl and xslt processor
	AM_CONDITIONAL([HAS_DOC_SUPPORT],
		[test "AS_VAR_GET(PERL)" != "no" -a "AS_VAR_GET(XSLTPROC)" != ""])

])
################################################################################
################################################################################
################################################################################
