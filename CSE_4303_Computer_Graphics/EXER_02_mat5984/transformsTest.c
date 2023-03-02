// Dalio, Brian A.
// dalioba
// 2022-08-22
//----------------------------------------------------------------
#include <stdio.h>

#include "matrix.h"
#include "transforms.h"

//----------------------------------------------------------------
static void matrixMultEachPoint( const char *name, const Matrix mtx );

//----------------------------------------------------------------
Point  pZero = { 0.0, 0.0, 0.0, 1.0 };
Point  pHalf = { 0.5, 0.5, 0.5, 1.0 };

Point  pX    = { 1.0, 0.0, 0.0, 1.0 };
Point  pXY   = { 1.0, 1.0, 0.0, 1.0 };
Point  pXZ   = { 1.0, 0.0, 1.0, 1.0 };

Point  pY    = { 0.0, 1.0, 0.0, 1.0 };
Point  pYZ   = { 0.0, 1.0, 1.0, 1.0 };

Point  pZ    = { 0.0, 0.0, 1.0, 1.0 };

Point  pXYZ  = { 1.0, 1.0, 1.0, 1.0 };

//----------------------------------------------------------------
int main()
{
  printf( "//-----------------------------------------------------------------\n" );
  printf( "//-- pZero ------------------\n" );
  dumpPoint( pZero );

  printf( "//-- pHalf ------------------\n" );
  dumpPoint( pHalf );

  printf( "//-- pX ---------------------\n" );
  dumpPoint( pX );

  printf( "\n//-- pXY --------------------\n" );
  dumpPoint( pXY );

  printf( "\n//-- pXZ --------------------\n" );
  dumpPoint( pXZ );

  printf( "\n//-- pY ---------------------\n" );
  dumpPoint( pY );

  printf( "\n//-- pYZ --------------------\n" );
  dumpPoint( pYZ );

  printf( "\n//-- pZ ---------------------\n" );
  dumpPoint( pZ );

  printf( "\n//-- pXYZ -------------------\n" );
  dumpPoint( pXYZ );

  printf( "\n//-----------------------------------------------------------------\n" );
  Matrix rotX;

  rotateXMatrix( DEG2RAD( 30.0 ), rotX );
  printf( "//-- rotX 30° ---------------\n" );
  dumpMatrix( rotX );

  matrixMultEachPoint( "(rotX 30°)", rotX );

  printf( "\n//-----------------------------------------------------------------\n" );
  Matrix rotY;

  rotateYMatrix( DEG2RAD( 45.0 ), rotY );
  printf( "//-- rotY 45° ---------------\n" );
  dumpMatrix( rotY );

  matrixMultEachPoint( "(rotY 45°)", rotY );

  printf( "\n//-----------------------------------------------------------------\n" );
  Matrix rotZ;

  rotateZMatrix( DEG2RAD( 60.0 ), rotZ );
  printf( "//-- rotZ 60° ---------------\n" );
  dumpMatrix( rotZ );

  matrixMultEachPoint( "(rotZ 60°)", rotZ );

  printf( "\n//-----------------------------------------------------------------\n" );
  Matrix scale;

  scaleMatrix( 4.5, 6.7, 8.9, scale );
  printf( "//-- scale 4.5, 6.7, 8.9 ----\n" );
  dumpMatrix( scale );

  matrixMultEachPoint( "scale", scale );

  printf( "\n//-----------------------------------------------------------------\n" );
  Matrix shearX;

  shearXMatrix( 1.2, 3.4, shearX );
  printf( "//-- shearX 1.2, 3.4 --------\n" );
  dumpMatrix( shearX );

  matrixMultEachPoint( "shearX", shearX );

  printf( "\n//-----------------------------------------------------------------\n" );
  Matrix shearY;

  shearYMatrix( 5.6, 7.8, shearY );
  printf( "//-- shearY 5.6, 7.8 --------\n" );
  dumpMatrix( shearY );

  matrixMultEachPoint( "shearY", shearY );

  printf( "\n//-----------------------------------------------------------------\n" );
  Matrix shearZ;

  shearZMatrix( 9.1, 2.3, shearZ );
  printf( "//-- shearZ 9.1, 2.3 --------\n" );
  dumpMatrix( shearZ );

  matrixMultEachPoint( "shearZ", shearZ );

  printf( "\n//-----------------------------------------------------------------\n" );
  Matrix shear;

  shearMatrix( 4.5, 6.7, 8.9, 0.1, 2.3, 4.5, shear );
  printf( "//-- shear 4.5, 6.7, 8.9, 0.1, 2.3, 4.5 --\n" );
  dumpMatrix( shear );

  matrixMultEachPoint( "shear", shear );

  printf( "\n//-----------------------------------------------------------------\n" );
  Matrix xlate;

  translateMatrix( 6.7, 8.9, 0.1, xlate );
  printf( "//-- xlate 6.7, 8.9, 0.1 ----\n" );
  dumpMatrix( xlate );

  matrixMultEachPoint( "xlate", xlate );

  printf( "\n//-----------------------------------------------------------------\n" );
  printf( "//-- Composition ------------\n" );
  Matrix composite;
  Matrix mTmp;

  copyMatrix( I4, composite );
  printf( "\n//-- subresult I4 -----------\n" );
  dumpMatrix( composite );

  matrixMultMatrix( composite, rotX,   mTmp );
  printf( "\n//-- subresult rotX ---------\n" );
  dumpMatrix( mTmp );

  matrixMultMatrix( mTmp,      rotY,   composite );
  printf( "\n//-- subresult rotY ---------\n" );
  dumpMatrix( composite );

  matrixMultMatrix( composite, rotZ,   mTmp );
  printf( "\n//-- subresult rotZ ---------\n" );
  dumpMatrix( mTmp );

  matrixMultMatrix( mTmp,      scale,  composite );
  printf( "\n//-- subresult scale --------\n" );
  dumpMatrix( composite );

  matrixMultMatrix( composite, shearX, mTmp );
  printf( "\n//-- subresult shearX -------\n" );
  dumpMatrix( mTmp );

  matrixMultMatrix( mTmp,      shearY, composite );
  printf( "\n//-- subresult shearY -------\n" );
  dumpMatrix( composite );

  matrixMultMatrix( composite, shearZ, mTmp );
  printf( "\n//-- subresult shearZ -------\n" );
  dumpMatrix( mTmp );

  matrixMultMatrix( mTmp,      shear, composite );
  printf( "\n//-- subresult shear --------\n" );
  dumpMatrix( composite );

  matrixMultMatrix( composite, xlate, mTmp );
  printf( "\n//-- subresult xlate --------\n" );
  dumpMatrix( mTmp );

  copyMatrix( mTmp, composite );
  printf( "\n//-- Final composite --------\n" );
  dumpMatrix( composite );

  matrixMultEachPoint( "composite", composite );

  printf( "\n//-----------------------------------------------------------------\n" );

  return 0;
}

//----------------------------------------------------------------
static void matrixMultEachPoint( const char *name, const Matrix mtx ) {
  Point pTmp;

  matrixMultPoint( mtx, pZero, pTmp );
  printf( "\n//-- %s·pZero ------------\n", name );
  dumpPoint( pTmp );

  matrixMultPoint( mtx, pHalf, pTmp );
  printf( "\n//-- %s·pHalf ------------\n", name );
  dumpPoint( pTmp );

  matrixMultPoint( mtx, pX, pTmp );
  printf( "\n//-- %s·pX ---------------\n", name );
  dumpPoint( pTmp );

  matrixMultPoint( mtx, pXY, pTmp );
  printf( "\n//-- %s·pXY --------------\n", name );
  dumpPoint( pTmp );

  matrixMultPoint( mtx, pXZ, pTmp );
  printf( "\n//-- %s·pXZ --------------\n", name );
  dumpPoint( pTmp );

  matrixMultPoint( mtx, pY, pTmp );
  printf( "\n//-- %s·pY ---------------\n", name );
  dumpPoint( pTmp );

  matrixMultPoint( mtx, pYZ, pTmp );
  printf( "\n//-- %s·pYZ --------------\n", name );
  dumpPoint( pTmp );

  matrixMultPoint( mtx, pZ, pTmp );
  printf( "\n//-- %s·pZ ---------------\n", name );
  dumpPoint( pTmp );

  matrixMultPoint( mtx, pXYZ, pTmp );
  printf( "\n//-- %s·pXYZ -------------\n", name );
  dumpPoint( pTmp );
}

//----------------------------------------------------------------
