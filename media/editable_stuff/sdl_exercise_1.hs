import Data.Word
import Data.Bits
import Foreign
import Control.Monad.State

import qualified Graphics.UI.SDL as SDL
import qualified Graphics.UI.SDL.Image as SDL_Image
import qualified System.Environment as SysEnv

-- Haaaaaack because I don't want to go to the extra bother of being able to maniuplate other kinds of images.
-- My goal, after all, isn't to be a general purpose image thingy. I can always convert stuff separately.
rShift = 0
gShift = 8
bShift = 16
aShift = 24
rMask = 255 `shift` rShift
gMask = 255 `shift` gShift
bMask = 255 `shift` bShift
aMask = 255 `shift` aShift

setR :: Word8 -> SDL.Pixel -> SDL.Pixel
setR new (SDL.Pixel pdata) = SDL.Pixel $ (pdata .&. complement rMask) + ((fromIntegral new) :: Word32) `shift` rShift
setG :: Word8 -> SDL.Pixel -> SDL.Pixel
setG new (SDL.Pixel pdata) = SDL.Pixel $ (pdata .&. complement gMask) + ((fromIntegral new) :: Word32) `shift` gShift
setB :: Word8 -> SDL.Pixel -> SDL.Pixel
setB new (SDL.Pixel pdata) = SDL.Pixel $ (pdata .&. complement bMask) + ((fromIntegral new) :: Word32) `shift` bShift
setA :: Word8 -> SDL.Pixel -> SDL.Pixel
setA new (SDL.Pixel pdata) = SDL.Pixel $ (pdata .&. complement aMask) + ((fromIntegral new) :: Word32) `shift` aShift
getR :: SDL.Pixel -> Word8
getR (SDL.Pixel pdata) = fromIntegral $ (pdata .&. rMask) `shift` (negate rShift)
getG :: SDL.Pixel -> Word8
getG (SDL.Pixel pdata) = fromIntegral $ (pdata .&. gMask) `shift` (negate gShift)
getB :: SDL.Pixel -> Word8
getB (SDL.Pixel pdata) = fromIntegral $ (pdata .&. bMask) `shift` (negate bShift)
getA :: SDL.Pixel -> Word8
getA (SDL.Pixel pdata) = fromIntegral $ (pdata .&. aMask) `shift` (negate aShift)

getPixel :: Int -> Int -> SDL.Surface -> IO SDL.Pixel
getPixel x y surf = do
  pixels <- castPtr `liftM` SDL.surfaceGetPixels surf
  SDL.Pixel `liftM` peekElemOff pixels (x + (y * SDL.surfaceGetWidth surf))

setPixel :: Int -> Int -> SDL.Pixel -> SDL.Surface -> IO ()
setPixel x y (SDL.Pixel pdata) surf = do
  pixels <- castPtr `liftM` SDL.surfaceGetPixels surf
  pokeElemOff pixels (x + (y * SDL.surfaceGetWidth surf)) pdata

main :: IO ()
main = do
    args <- SysEnv.getArgs
    case args of
      []     -> print "Please give an image path name"
      name:_ -> hackAround name

hackAround :: String -> IO ()
hackAround filename = SDL.withInit [SDL.InitEverything] $ do
    SDL.setVideoMode 640 640 32 []
    SDL.setCaption "wait why am I setting a caption" "this is pointless"
    screen <- SDL.getVideoSurface
    image <- SDL_Image.load filename
    sequence [do
      pixel <- getPixel x y image
      setPixel x y (setR 255 . setA 128 . setB (getG pixel) $ pixel) image |
      x <- [0..(SDL.surfaceGetWidth image - 1)],
      y <- [0..(SDL.surfaceGetHeight image - 1)]]
    SDL.saveBMP image "output.bmp"
    let
      loop 30 = return ()
      loop i = do
        SDL.blitSurface image (Just $ SDL.Rect 0 0 (SDL.surfaceGetWidth image) (SDL.surfaceGetHeight image)) screen (Just $ SDL.Rect (10+(10*i)) (10+(5*i)) 0 0)
        SDL.flip screen
        SDL.delay 500
        loop (i + 1)
      in loop 0

