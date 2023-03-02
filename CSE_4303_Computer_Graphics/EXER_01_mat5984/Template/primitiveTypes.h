// Dalio, Brian A.
// dalioba
// 2022-08-22
//----------------------------------------------------------------
#if !defined( __PRIMITIVE_TYPES_H__ )
#define __PRIMITIVE_TYPES_H__

//----------------------------------------------------------------
#include <float.h>

#if DBL_MANT_DIG == 53

#define FLOAT64_IS_DOUBLE
typedef double FLOAT64;

#elif LDBL_MANT_DIG == 53

#define FLOAT64_IS_LONG_DOUBLE
typedef long double FLOAT64;

#else
#error "Can't determine which type to use for FLOAT64?"

#endif

//----------------------------------------------------------------
#endif
