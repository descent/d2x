noinst_LIBRARIES = lib2d.a
INCLUDES = -I $(top_srcdir)/include

if USE_ASM
ASM_SRCS =
else
ASM_SRCS = tmerge.c
endif

if MACDATA
TRANSPARENCY_COLOR = 0
else
TRANSPARENCY_COLOR = 255
endif

lib2d_a_SOURCES = ${ASM_SRCS} \
2dsline.c  box.c     disc.c    ibitblt.c  pcx.c    rect.c   scalec.c \
bitblt.c   canvas.c  font.c    line.c	  pixel.c  rle.c \
bitmap.c   circle.c  gpixel.c  palette.c  poly.c

SUFFIXES = .asm
%.o: %.asm
	$(NASM) -dTRANSPARENCY_COLOR=${TRANSPARENCY_COLOR} $(NASMFLAGS) $< -o $@

if USE_ASM
lib2d_a_LIBADD = linear.o tmerge_a.o
endif

EXTRA_DIST = \
linear.asm scalea.asm tmerge_a.asm \
bitmap.h clip.h scalea.h \
scale.c tmerge.c
