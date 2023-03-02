// Trinh, Minh
// mat5984
// 2023-02-02
//----------------------------------------------------------------
#include <stdio.h>

#include "matrix.h"

//----------------------------------------------------------------
const Matrix I4 = {
    { 1, 0, 0, 0 },
    { 0, 1, 0, 0 },
    { 0, 0, 1, 0 },
    { 0, 0, 0, 1 } };

const Matrix Z4 = {
    { 0, 0, 0, 0 },
    { 0, 0, 0, 0 },
    { 0, 0, 0, 0 },
    { 0, 0, 0, 0 } };

//----------------------------------------------------------------
void matrixPlusMatrix( const Matrix a, const Matrix b, Matrix c )
{
  FLOAT64 *ap = (FLOAT64 *) a;
  FLOAT64 *bp = (FLOAT64 *) b;
  FLOAT64 *cp = (FLOAT64 *) c;

  for ( int i = 0; i < 16; i++ ) {
    *cp++ = *ap++ + *bp++;
  }
}

//----------------------------------------------------------------
void copyMatrix( const Matrix a, Matrix b )
{
  FLOAT64 *ap = (FLOAT64 *) a;
  FLOAT64 *bp = (FLOAT64 *) b;

  for ( int i = 0; i < 16; i++ ) {
    *bp++ = *ap++;
  }
}

//----------------------------------------------------------------
void matrixMultMatrix( const Matrix a, const Matrix b, Matrix c )
{
  for ( int row = 0; row < 4; row++ ) {
    for ( int col = 0; col < 4; col++ ) {
      // TODO: Compute c[row][col] as the sum of four multiplies,
      //        each of which is a[row][?] times b[?][col].
      c[row][col] = 0;
      for ( int elem = 0; elem < 4; elem++) {
        c[row][col] += a[row][elem]*b[elem][col];
      }
    }
  }
}

//----------------------------------------------------------------
void matrixMultPoint( const Matrix a, const Point b, Point c )
{
  for ( int row = 0; row < 4; row++ ) {
    // TODO: Compute c[row] as the sum of four multiplies, each
    //        of which is a[row][?] times b[?].
    c[row] = 0;
    for ( int elem = 0; elem < 4; elem++) {
      c[row] += a[row][elem]*b[elem];
    }
  }
}

//----------------------------------------------------------------
void scalarMultMatrix( FLOAT64 s, const Matrix a, Matrix b )
{
  FLOAT64 *ap = (FLOAT64 *) a;
  FLOAT64 *bp = (FLOAT64 *) b;

  for ( int i = 0; i < 16; i++ ) {
    // TODO: Compute *bp++ as the product of s and *ap++.
    *bp++ = s * *ap++;
  }
}

//----------------------------------------------------------------
void scalarMultPoint( FLOAT64 s, const Point a, Point b )
{
  // TODO: Compute each of b[0] through b[3] using the scalar s
  //        and a[0] through a[3].
  for ( int elem = 0; elem < 4; elem++) {
    b[elem] = s*a[elem];
  }
}

//----------------------------------------------------------------
void dumpMatrix( const Matrix m ) { fdumpfMatrix( stdout, m, ELEMENT_DEFAULT_FORMAT ); }
void dumpfMatrix( const Matrix m, const char *fmt ) { fdumpfMatrix( stdout, m, fmt ); }
void fdumpMatrix( FILE *fp, const Matrix m ) { fdumpfMatrix( fp, m, ELEMENT_DEFAULT_FORMAT ); }

void fdumpfMatrix( FILE *fp, const Matrix m, const char *fmt )
{
  for ( int r = 0; r < 4; r++ ) {
    fprintf( fp, fmt, m[r][0] );
    fputc( ' ', fp );
    fprintf( fp, fmt, m[r][1] );
    fputc( ' ', fp );
    fprintf( fp, fmt, m[r][2] );
    fputc( ' ', fp );
    fprintf( fp, fmt, m[r][3] );
    fputc( '\n', fp );
  }
}

//----------------------------------------------------------------
void dumpPoint( const Point p ) { fdumpfPoint( stdout, p, ELEMENT_DEFAULT_FORMAT ); }
void dumpfPoint( const Point p, const char *fmt ) { fdumpfPoint( stdout, p, fmt ); }
void fdumpPoint( FILE *fp, const Point p ) { fdumpfPoint( fp, p, ELEMENT_DEFAULT_FORMAT ); }

void fdumpfPoint( FILE *fp, const Point p, const char *fmt )
{
  fprintf( fp, fmt, p[0] );
  fputc( '\n', fp );
  fprintf( fp, fmt, p[1] );
  fputc( '\n', fp );
  fprintf( fp, fmt, p[2] );
  fputc( '\n', fp );
  fprintf( fp, fmt, p[3] );
  fputc( '\n', fp );
}

//----------------------------------------------------------------
