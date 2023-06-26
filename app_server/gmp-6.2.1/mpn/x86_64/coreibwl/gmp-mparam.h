/* Broadwell gmp-mparam.h -- Compiler/machine parameter header file.

Copyright 2019 Free Software Foundation, Inc.

This file is part of the GNU MP Library.

The GNU MP Library is free software; you can redistribute it and/or modify
it under the terms of either:

  * the GNU Lesser General Public License as published by the Free
    Software Foundation; either version 3 of the License, or (at your
    option) any later version.

or

  * the GNU General Public License as published by the Free Software
    Foundation; either version 2 of the License, or (at your option) any
    later version.

or both in parallel, as here.

The GNU MP Library is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
for more details.

You should have received copies of the GNU General Public License and the
GNU Lesser General Public License along with the GNU MP Library.  If not,
see https://www.gnu.org/licenses/.  */

#define GMP_LIMB_BITS 64
#define GMP_LIMB_BYTES 8

/* Disable use of slow functions.  FIXME: We should disable lib inclusion.  */
#undef HAVE_NATIVE_mpn_mul_2
#undef HAVE_NATIVE_mpn_addmul_2

/* 3400-3800 MHz Intel Xeon E3-1285Lv4 Broadwell */
/* FFT tuning limit = 467,964,472 */
/* Generated by tuneup.c, 2019-10-17, gcc 8.3 */

#define MOD_1_NORM_THRESHOLD                 0  /* always */
#define MOD_1_UNNORM_THRESHOLD               0  /* always */
#define MOD_1N_TO_MOD_1_1_THRESHOLD          4
#define MOD_1U_TO_MOD_1_1_THRESHOLD          3
#define MOD_1_1_TO_MOD_1_2_THRESHOLD        14
#define MOD_1_2_TO_MOD_1_4_THRESHOLD        24
#define PREINV_MOD_1_TO_MOD_1_THRESHOLD      9
#define USE_PREINV_DIVREM_1                  1  /* native */
#define DIV_QR_1_NORM_THRESHOLD              1
#define DIV_QR_1_UNNORM_THRESHOLD        MP_SIZE_T_MAX  /* never */
#define DIV_QR_2_PI2_THRESHOLD              24
#define DIVEXACT_1_THRESHOLD                 0  /* always (native) */
#define BMOD_1_TO_MOD_1_THRESHOLD           22

#define DIV_1_VS_MUL_1_PERCENT             455

#define MUL_TOOM22_THRESHOLD                26
#define MUL_TOOM33_THRESHOLD                73
#define MUL_TOOM44_THRESHOLD               202
#define MUL_TOOM6H_THRESHOLD               303
#define MUL_TOOM8H_THRESHOLD               406

#define MUL_TOOM32_TO_TOOM43_THRESHOLD     141
#define MUL_TOOM32_TO_TOOM53_THRESHOLD     152
#define MUL_TOOM42_TO_TOOM53_THRESHOLD     137
#define MUL_TOOM42_TO_TOOM63_THRESHOLD     151
#define MUL_TOOM43_TO_TOOM54_THRESHOLD     198

#define SQR_BASECASE_THRESHOLD               0  /* always (native) */
#define SQR_TOOM2_THRESHOLD                 34
#define SQR_TOOM3_THRESHOLD                117
#define SQR_TOOM4_THRESHOLD                336
#define SQR_TOOM6_THRESHOLD                426
#define SQR_TOOM8_THRESHOLD                547

#define MULMID_TOOM42_THRESHOLD             46

#define MULMOD_BNM1_THRESHOLD               16
#define SQRMOD_BNM1_THRESHOLD               18

#define MUL_FFT_MODF_THRESHOLD             460  /* k = 5 */
#define MUL_FFT_TABLE3                                      \
  { {    460, 5}, {     21, 6}, {     11, 5}, {     23, 6}, \
    {     12, 5}, {     25, 6}, {     25, 7}, {     13, 6}, \
    {     28, 7}, {     15, 6}, {     31, 7}, {     25, 8}, \
    {     13, 7}, {     28, 8}, {     15, 7}, {     31, 8}, \
    {     17, 7}, {     35, 8}, {     19, 7}, {     39, 8}, \
    {     21, 9}, {     11, 8}, {     27, 9}, {     15, 8}, \
    {     35, 9}, {     19, 8}, {     41, 9}, {     23, 8}, \
    {     49, 9}, {     27,10}, {     15, 9}, {     39, 8}, \
    {     79,10}, {     23, 9}, {     55,11}, {     15,10}, \
    {     31, 9}, {     71,10}, {     39, 9}, {     83,10}, \
    {     47, 9}, {     99,10}, {     55,11}, {     31,10}, \
    {     87,11}, {     47,10}, {    103,12}, {     31,11}, \
    {     63,10}, {    135,11}, {     79,10}, {    167,11}, \
    {     95,10}, {    199,11}, {    111,12}, {     63, 8}, \
    {   1087,10}, {    287, 9}, {    575,10}, {    303,11}, \
    {    159,12}, {     95,11}, {    191,10}, {    383,13}, \
    {     63,12}, {    127,11}, {    255,10}, {    511,11}, \
    {    271,10}, {    543,11}, {    287,10}, {    575,11}, \
    {    303,10}, {    607,12}, {    159,11}, {    319,10}, \
    {    639,11}, {    335,10}, {    671,11}, {    351,10}, \
    {    703,11}, {    367,12}, {    191,11}, {    383,10}, \
    {    767,11}, {    415,10}, {    831,11}, {    447,13}, \
    {    127,12}, {    255,11}, {    543,12}, {    287,11}, \
    {    607,12}, {    319,11}, {    671,12}, {    351,11}, \
    {    703,13}, {    191,12}, {    383,11}, {    767,12}, \
    {    415,11}, {    831,12}, {    447,14}, {    127,13}, \
    {    255,12}, {    607,13}, {    319,12}, {    735,13}, \
    {    383,12}, {    831,13}, {    447,12}, {    959,14}, \
    {    255,13}, {    511,12}, {   1023,13}, {    575,12}, \
    {   1151,13}, {    639,12}, {   1279,13}, {    703,14}, \
    {    383,13}, {    831,12}, {   1663,13}, {    959,14}, \
    {    511,13}, {   1087,12}, {   2175,13}, {   1151,14}, \
    {    639,13}, {   1279,12}, {   2559,13}, {   1343,12}, \
    {   2687,13}, {   1407,14}, {    767,13}, {   1535,12}, \
    {   3071,13}, {   1599,12}, {   3199,13}, {   1663,14}, \
    {    895,15}, {    511,14}, {   1023,13}, {   2175,14}, \
    {   1151,13}, {   2431,12}, {   4863,14}, {   1279,13}, \
    {   2687,14}, {   1407,15}, {    767,14}, {   1535,13}, \
    {   3199,14}, {   1663,13}, {   3455,12}, {   6911,16}, \
    {    511,15}, {   1023,14}, {   2175,13}, {   4479,14}, \
    {   2303,13}, {   4607,14}, {   2431,13}, {   4863,15}, \
    {   1279,14}, {   2815,13}, {   5631,14}, {   2943,13}, \
    {   5887,15}, {   1535,14}, {   3455,13}, {   6911,15}, \
    {   1791,14}, {   3839,13}, {   7679,16}, {   1023,15}, \
    {   2047,14}, {   4479,15}, {   2303,14}, {   4863,15}, \
    {   2559,14}, {   5247,15}, {   2815,14}, {   5887,16}, \
    {   1535,15}, {   3327,14}, {   6911,15}, {   3839,14}, \
    {   7679,17}, {   1023,16}, {   2047,15}, {   4351,14}, \
    {   8703,15}, {   4863,16}, {   2559,15}, {   5887,14}, \
    {  11775,16}, {   3071,15}, {   6911,16}, {   3583,15}, \
    {   7679,14}, {  15359,17}, {   2047,16}, {   4095,15}, \
    {   8703,16}, {   4607,15}, {   9983,14}, {  19967,16}, \
    {   5631,15}, {  11775,17}, {   3071,16}, {  65536,17}, \
    { 131072,18}, { 262144,19}, { 524288,20}, {1048576,21}, \
    {2097152,22}, {4194304,23}, {8388608,24} }
#define MUL_FFT_TABLE3_SIZE 219
#define MUL_FFT_THRESHOLD                 5760

#define SQR_FFT_MODF_THRESHOLD             400  /* k = 5 */
#define SQR_FFT_TABLE3                                      \
  { {    400, 5}, {     23, 6}, {     12, 5}, {     25, 6}, \
    {     28, 7}, {     15, 6}, {     31, 7}, {     25, 8}, \
    {     13, 7}, {     27, 8}, {     15, 7}, {     31, 8}, \
    {     17, 7}, {     35, 8}, {     19, 7}, {     39, 8}, \
    {     27, 9}, {     15, 8}, {     35, 9}, {     19, 8}, \
    {     41, 9}, {     23, 8}, {     47, 9}, {     27,10}, \
    {     15, 9}, {     39,10}, {     23, 9}, {     51,11}, \
    {     15,10}, {     31, 9}, {     67,10}, {     39, 9}, \
    {     79,10}, {     47, 9}, {     95,10}, {     55,11}, \
    {     31,10}, {     79,11}, {     47,10}, {     95,12}, \
    {     31,11}, {     63,10}, {    127,11}, {     79,10}, \
    {    159,11}, {     95,12}, {     63,11}, {    127,10}, \
    {    255, 9}, {    511,11}, {    143,10}, {    287, 9}, \
    {    575,10}, {    303,11}, {    159,10}, {    319,12}, \
    {     95, 8}, {   1599, 9}, {    831,11}, {    223,10}, \
    {    447,12}, {    127,11}, {    255,10}, {    511,11}, \
    {    271,10}, {    543,11}, {    287,10}, {    575,11}, \
    {    303,10}, {    607,12}, {    159,11}, {    319,10}, \
    {    639,11}, {    335,10}, {    671,11}, {    351,10}, \
    {    703,11}, {    367,10}, {    735,11}, {    415,10}, \
    {    831,12}, {    223,11}, {    447,13}, {    127,12}, \
    {    255,11}, {    543,12}, {    287,11}, {    607,12}, \
    {    319,11}, {    671,12}, {    351,11}, {    735,12}, \
    {    383,11}, {    767,12}, {    415,11}, {    831,12}, \
    {    447,14}, {    127,13}, {    255,12}, {    607,13}, \
    {    319,12}, {    735,13}, {    383,12}, {    799,13}, \
    {    447,12}, {    959,13}, {    511,12}, {   1023,13}, \
    {    575,12}, {   1151,13}, {    639,12}, {   1279,13}, \
    {    703,14}, {    383,13}, {    767,12}, {   1535,13}, \
    {    831,12}, {   1663,13}, {    959,14}, {    511,13}, \
    {   1087,12}, {   2175,13}, {   1151,14}, {    639,13}, \
    {   1343,12}, {   2687,13}, {   1407,12}, {   2815,13}, \
    {   1471,14}, {    767,13}, {   1599,12}, {   3199,13}, \
    {   1663,14}, {    895,15}, {    511,14}, {   1023,13}, \
    {   2175,14}, {   1151,13}, {   2431,12}, {   4863,14}, \
    {   1279,13}, {   2687,14}, {   1407,13}, {   2815,15}, \
    {    767,14}, {   1535,13}, {   3199,14}, {   1663,13}, \
    {   3455,12}, {   6911,14}, {   1791,16}, {    511,15}, \
    {   1023,14}, {   2047,13}, {   4095,14}, {   2175,13}, \
    {   4351,14}, {   2303,13}, {   4607,14}, {   2431,13}, \
    {   4863,15}, {   1279,14}, {   2943,13}, {   5887,15}, \
    {   1535,14}, {   3455,13}, {   6911,15}, {   1791,14}, \
    {   3839,13}, {   7679,16}, {   1023,15}, {   2047,14}, \
    {   4351,15}, {   2303,14}, {   4863,15}, {   2559,14}, \
    {   5247,15}, {   2815,14}, {   5887,16}, {   1535,15}, \
    {   3327,14}, {   6911,15}, {   3839,14}, {   7679,17}, \
    {   1023,16}, {   2047,15}, {   4863,16}, {   2559,15}, \
    {   5887,14}, {  11775,16}, {   3071,15}, {   6911,16}, \
    {   3583,15}, {   7679,14}, {  15359,15}, {   7935,17}, \
    {   2047,16}, {   4095,15}, {   8447,16}, {   4607,15}, \
    {   9471,14}, {  18943,15}, {   9983,14}, {  19967,16}, \
    {   5631,15}, {  11775,17}, {   3071,16}, {  65536,17}, \
    { 131072,18}, { 262144,19}, { 524288,20}, {1048576,21}, \
    {2097152,22}, {4194304,23}, {8388608,24} }
#define SQR_FFT_TABLE3_SIZE 215
#define SQR_FFT_THRESHOLD                 3712

#define MULLO_BASECASE_THRESHOLD             0  /* always */
#define MULLO_DC_THRESHOLD                  80
#define MULLO_MUL_N_THRESHOLD            11025
#define SQRLO_BASECASE_THRESHOLD             9
#define SQRLO_DC_THRESHOLD                 109
#define SQRLO_SQR_THRESHOLD               7293

#define DC_DIV_QR_THRESHOLD                 54
#define DC_DIVAPPR_Q_THRESHOLD             183
#define DC_BDIV_QR_THRESHOLD                86
#define DC_BDIV_Q_THRESHOLD                160

#define INV_MULMOD_BNM1_THRESHOLD           58
#define INV_NEWTON_THRESHOLD               171
#define INV_APPR_THRESHOLD                 171

#define BINV_NEWTON_THRESHOLD              292
#define REDC_1_TO_REDC_2_THRESHOLD          33
#define REDC_2_TO_REDC_N_THRESHOLD          63

#define MU_DIV_QR_THRESHOLD               1589
#define MU_DIVAPPR_Q_THRESHOLD            1589
#define MUPI_DIV_QR_THRESHOLD               67
#define MU_BDIV_QR_THRESHOLD              1470
#define MU_BDIV_Q_THRESHOLD               1866

#define POWM_SEC_TABLE  2,10,191,494,712,1378

#define GET_STR_DC_THRESHOLD                12
#define GET_STR_PRECOMPUTE_THRESHOLD        20
#define SET_STR_DC_THRESHOLD               644
#define SET_STR_PRECOMPUTE_THRESHOLD      1658

#define FAC_DSC_THRESHOLD                  562
#define FAC_ODD_THRESHOLD                   48

#define MATRIX22_STRASSEN_THRESHOLD         16
#define HGCD2_DIV1_METHOD                    5  /* 0.38% faster than 3 */
#define HGCD_THRESHOLD                      73
#define HGCD_APPR_THRESHOLD                 67
#define HGCD_REDUCE_THRESHOLD             3014
#define GCD_DC_THRESHOLD                   630
#define GCDEXT_DC_THRESHOLD                365
#define JACOBI_BASE_METHOD                   1  /* 29.65% faster than 4 */

/* Tuneup completed successfully, took 239050 seconds */
