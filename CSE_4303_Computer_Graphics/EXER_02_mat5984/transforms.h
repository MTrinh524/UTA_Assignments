// Dalio, Brian A.
// dalioba
// 2022-08-22
//----------------------------------------------------------------
#if !defined( __TRANSFORMS_H__ )
#define __TRANSFORMS_H__

//----------------------------------------------------------------
#include <math.h>

#include "matrix.h"

#if !defined( RAD2DEG )
#define RAD2DEG(r) (M_1_PI*180.0*(r))
#endif

#if !defined( DEG2RAD )
#define DEG2RAD(d) (M_PI*(d)/180.0)
#endif

//----------------------------------------------------------------
extern void rotateXMatrix( const FLOAT64 theta, Matrix xform );
extern void rotateYMatrix( const FLOAT64 theta, Matrix xform );
extern void rotateZMatrix( const FLOAT64 theta, Matrix xform );

extern void scaleMatrix( const FLOAT64 sx, const FLOAT64 sy, const FLOAT64 sz, Matrix xform );

extern void shearXMatrix( const FLOAT64 hxy, const FLOAT64 hxz, Matrix xform );
extern void shearYMatrix( const FLOAT64 hyx, const FLOAT64 hyz, Matrix xform );
extern void shearZMatrix( const FLOAT64 hzx, const FLOAT64 hzy, Matrix xform );

extern void shearMatrix( const FLOAT64 hxy, const FLOAT64 hxz, const FLOAT64 hyx, const FLOAT64 hyz, const FLOAT64 hzx, const FLOAT64 hzy, Matrix xform );

extern void translateMatrix( const FLOAT64 tx, const FLOAT64 ty, const FLOAT64 tz, Matrix xform );

//----------------------------------------------------------------
#endif
