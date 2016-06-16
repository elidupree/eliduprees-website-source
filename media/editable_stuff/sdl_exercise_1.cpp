#include <cstdlib>
#include "SDL.h"
#include "SDL_image.h"
#include <string>
#include <inttypes.h>
#include <iostream>

class Image {
public:
  Image(SDL_Surface *internal):internal(internal){  }
  int getr(int x, int y)const;
  int getg(int x, int y)const;
  int getb(int x, int y)const;
  int geta(int x, int y)const;
  void setr(int x, int y, uint8_t val);
  void setg(int x, int y, uint8_t val);
  void setb(int x, int y, uint8_t val);
  void seta(int x, int y, uint8_t val);
private:
  uint32_t& getpixel(int x, int y);
  uint32_t const& getpixel(int x, int y)const;
  SDL_PixelFormat const* fmt()const { return internal->format; }
  SDL_Surface *internal;
};

uint32_t& Image::getpixel(int x, int y) {
  return ((uint32_t*)(internal->pixels))[x + y*internal->w];
}
uint32_t const& Image::getpixel(int x, int y)const {
  return ((uint32_t*)(internal->pixels))[x + y*internal->w];
}

int Image::getr(int x, int y)const {
  return (((getpixel(x, y) & fmt()->Rmask) >> fmt()->Rshift) << fmt()->Rloss);
}
int Image::getg(int x, int y)const {
  return (((getpixel(x, y) & fmt()->Gmask) >> fmt()->Gshift) << fmt()->Gloss);
}
int Image::getb(int x, int y)const {
  return (((getpixel(x, y) & fmt()->Bmask) >> fmt()->Bshift) << fmt()->Bloss);
}
int Image::geta(int x, int y)const {
  return (((getpixel(x, y) & fmt()->Amask) >> fmt()->Ashift) << fmt()->Aloss);
}
void Image::setr(int x, int y, uint8_t val) {
  getpixel(x, y) = (getpixel(x, y) & ~(fmt()->Rmask)) + ((val >> fmt()->Rloss) << fmt()->Rshift);
}
void Image::setg(int x, int y, uint8_t val) {
  getpixel(x, y) = (getpixel(x, y) & ~(fmt()->Gmask)) + ((val >> fmt()->Gloss) << fmt()->Gshift);
}
void Image::setb(int x, int y, uint8_t val) {
  getpixel(x, y) = (getpixel(x, y) & ~(fmt()->Bmask)) + ((val >> fmt()->Bloss) << fmt()->Bshift);
}
void Image::seta(int x, int y, uint8_t val) {
  getpixel(x, y) = (getpixel(x, y) & ~(fmt()->Amask)) + ((val >> fmt()->Aloss) << fmt()->Ashift);
}

 
int main(int argc, char **argv) {
  if (argc < 2) {
    std::cerr << "Please give an image path name\n";
    return 1;
  }

  if (SDL_Init(SDL_INIT_VIDEO) != 0) {
    std::cerr << "SDL_Init(SDL_INIT_VIDEO) failed: " << SDL_GetError() << "\n";
    return 1;
  }
  atexit(SDL_Quit);
  
  SDL_Surface *screen = SDL_SetVideoMode(640, 640, 32, 0x0);
  if (screen == NULL) {
    std::cerr << "SDL_SetVideoMode failed: " << SDL_GetError() << "\n";
    return 1;
  }

  SDL_Surface *img = IMG_Load(argv[1]);
  if (img == NULL) {
    std::cerr << "Error: file could not be opened: " << IMG_GetError() << "\n";
    return 1;
  }

  SDL_LockSurface(img);
  Image superimg(img);
  for (int x = 0; x < img->w; ++x) {
    for (int y = 0; y < img->w; ++y) {
      superimg.setr(x, y, 255);
      superimg.setb(x, y, superimg.getg(x, y));
      superimg.seta(x, y, 128);
    }
  }
  SDL_UnlockSurface(img);

  SDL_SaveBMP(img, "output.bmp");
  for (int i = 0; i < 30; ++i) {
    SDL_Rect src, dst;
 
    src.x = 0;  src.y = 0;  src.w = img->w;  src.h = img->h;
    dst.x = 10+10*i;  dst.y = 10+5*i;  dst.w = 0;  dst.h = 0;
    SDL_BlitSurface(img, &src, screen, &dst);
    SDL_Flip(screen);
    SDL_Delay(500);
  }
 
  SDL_FreeSurface(img);
  return 0;
}

