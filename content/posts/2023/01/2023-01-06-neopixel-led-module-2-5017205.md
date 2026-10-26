+++
date = "2023-01-06T08:00:00"
draft = false
title = "NeoPixel 的なLEDモジュールを買う -2-"
description = "NeoPixel互換モジュールをFastLEDとArduinoで点灯し、動作を比較する。"

[taxonomies]
tags = ["NeoPixel", "WS2812", "FastLED", "Arduino", "2023-01"]

[extra]
image = "/2023-01-06/5017205-title.jpeg"
+++

　NeoPixel というのは Adafruit の多色LEDモジュールに付けた製品シリーズ名。それに使われていたLEDがWorldSemi社のWS2812。WS2812は最初は６ピンだったのだけど、のちに４ピンで動作するWS2812Bが使われるようになった。

> NeoPixels Products Category on Adafruit Industries<br>
> <https://www.adafruit.com/category/168>

![](/2023-01-06/5017205-01.png)

　Arduino向けのAdafruit純正ライブラリはこれ。

> GitHub - adafruit/Adafruit_NeoPixel: Arduino library for controlling single-wire LED pixels (NeoPixel, WS2812, etc.)<br>
> <https://github.com/adafruit/Adafruit_NeoPixel>

　シリアル接続で制御できるLEDは、WorldSemi社のWS2812シリーズ製品がデファクトスタンダードになっている。

> WORLDSEMI CO., LIMITED<br>
> <http://www.world-semi.com/>

![](/2023-01-06/5017205-02.png)

　素のWS2812は、本家では、もう出荷してない感じかな。

![](/2023-01-06/5017205-03.png)

　でも、どれを見ても、今回買ったモジュールで使われているものとは違う感じ。互換品は、各社から出ているのでよくわからない。SK6812とかXT1511などの互換品でもWS2812やWS2812Bと型番が書かれているので、現物を見ないと判別はできない。

　SK6812は、Normand社が製品化している。

> Shenzhen Normand Electronic Co.,Ltd<br>
> <http://www.normandled.com/>

![](/2023-01-06/5017205-04.png)

　今回は、AdafruitのNeoPixcelライブラリを使用せずに、より汎用のFastLEDを使うことにする。

> GitHub - FastLED/FastLED: The FastLED library for colored LED animation on Arduino. Please direct questions/requests for help to the FastLED Reddit community: http://fastled.io/r We'd like to use github "issues" just for tracking library bugs / enhancements.<br>
> <https://github.com/FastLED/FastLED>

　ArduinoIDEのライブラリマネージャからFastLEDライブラリをインストールする。

![](/2023-01-06/5017205-05.png)

![](/2023-01-06/5017205-06.png)

　FastLEDライブラリのサンプルスケッチは、以下のようになっていた。基本的なBlinkのスケッチを開いてみる。

![](/2023-01-06/5017205-07.png)

　コメント化されている部分が多くあるけれど、実際のコードはこれだけ。LEDの数を指定して、ピン３でGPIO接続して、LEDの数だけ初期化を行って、赤く点灯、消灯を繰り返すだけ。CLOCK_PINはWS2812では使っていないので、使用していない。削除しても動作には問題ない。

```cpp
#include <FastLED.h>
#define NUM_LEDS 1
#define DATA_PIN 3
#define CLOCK_PIN 13
CRGB leds[NUM_LEDS];
void setup() {
FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
}
void loop() {
leds[0] = CRGB::Red;
FastLED.show();
delay(500);
leds[0] = CRGB::Black;
FastLED.show();
delay(500);
}
```

　UNOモドキにLEDモジュールを接続する。

![](/2023-01-06/5017205-08.png)

　スケッチを書き込むと、１つのLEDが赤色で点滅する。

![](/2023-01-06/5017205-09.png)

![](/2023-01-06/5017205-10.png)

　モジュールの指定をコメントアウトされていたWS2812Bにすると、緑で点滅した。なんだこれ？

```cpp
FastLED.addLeds<WS2812B, DATA_PIN, RGB>(leds, NUM_LEDS);
```

　NUM_LEDSを７にしても動作が変わらない。点灯するのは１つだけ。うむむ？

　初期不良品かな？

　確認のため、前に買ってあったモジュールにしてみても１つしか点滅しない。これはわからないな...

　別のスケッチを試してみる。サンプルスケッチの中から、ColorPalletを使ってみる。

　サンプルスケッチだというのに、スケッチによって使っているピンの番号が違うのはどういうわけかな... 作者が違うのでしょうがない？

　前に買ってあったモジュールでは、正常に動作した。別のテープ状のもの、これはスイッチサイエンスで買ったものなので純正のWS2812Bだろう、それも正常に動作した。

![](/2023-01-06/5017205-11.png)

![](/2023-01-06/5017205-12.png)

![](/2023-01-06/5017205-13.png)

　スケッチのデフォルト値の64では、輝度が高すぎて直視がつらいので、10くらいでもいい感じ。

![](/2023-01-06/5017205-14.png)

```cpp
#include <FastLED.h>
//#define LED_PIN     5
#define LED_PIN     3
//#define NUM_LEDS    50
#define NUM_LEDS    10
//#define BRIGHTNESS  64
#define BRIGHTNESS  10
#define LED_TYPE    WS2811
#define COLOR_ORDER GRB
CRGB leds[NUM_LEDS];
#define UPDATES_PER_SECOND 100
CRGBPalette16 currentPalette;
TBlendType    currentBlending;
extern CRGBPalette16 myRedWhiteBluePalette;
extern const TProgmemPalette16 myRedWhiteBluePalette_p PROGMEM;
void setup() {
delay( 3000 ); // power-up safety delay
FastLED.addLeds<LED_TYPE, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS).setCorrection( TypicalLEDStrip );
FastLED.setBrightness(  BRIGHTNESS );
currentPalette = RainbowColors_p;
currentBlending = LINEARBLEND;
}
void loop()
{
ChangePalettePeriodically();
static uint8_t startIndex = 0;
startIndex = startIndex + 1; /* motion speed */
FillLEDsFromPaletteColors( startIndex);
FastLED.show();
FastLED.delay(1000 / UPDATES_PER_SECOND);
}
void FillLEDsFromPaletteColors( uint8_t colorIndex)
{
uint8_t brightness = 255;
for( int i = 0; i < NUM_LEDS; ++i) {
leds[i] = ColorFromPalette( currentPalette, colorIndex, brightness, currentBlending);
colorIndex += 3;
}
}
void ChangePalettePeriodically()
{
uint8_t secondHand = (millis() / 1000) % 60;
static uint8_t lastSecond = 99;
if( lastSecond != secondHand) {
lastSecond = secondHand;
if( secondHand ==  0)  { currentPalette = RainbowColors_p;         currentBlending = LINEARBLEND; }
if( secondHand == 10)  { currentPalette = RainbowStripeColors_p;   currentBlending = NOBLEND;  }
if( secondHand == 15)  { currentPalette = RainbowStripeColors_p;   currentBlending = LINEARBLEND; }
if( secondHand == 20)  { SetupPurpleAndGreenPalette();             currentBlending = LINEARBLEND; }
if( secondHand == 25)  { SetupTotallyRandomPalette();              currentBlending = LINEARBLEND; }
if( secondHand == 30)  { SetupBlackAndWhiteStripedPalette();       currentBlending = NOBLEND; }
if( secondHand == 35)  { SetupBlackAndWhiteStripedPalette();       currentBlending = LINEARBLEND; }
if( secondHand == 40)  { currentPalette = CloudColors_p;           currentBlending = LINEARBLEND; }
if( secondHand == 45)  { currentPalette = PartyColors_p;           currentBlending = LINEARBLEND; }
if( secondHand == 50)  { currentPalette = myRedWhiteBluePalette_p; currentBlending = NOBLEND;  }
if( secondHand == 55)  { currentPalette = myRedWhiteBluePalette_p; currentBlending = LINEARBLEND; }
}
}
void SetupTotallyRandomPalette()
{
for( int i = 0; i < 16; ++i) {
currentPalette[i] = CHSV( random8(), 255, random8());
}
}
void SetupBlackAndWhiteStripedPalette()
{
// 'black out' all 16 palette entries...
fill_solid( currentPalette, 16, CRGB::Black);
// and set every fourth one to white.
currentPalette[0] = CRGB::White;
currentPalette[4] = CRGB::White;
currentPalette[8] = CRGB::White;
currentPalette[12] = CRGB::White;
}
void SetupPurpleAndGreenPalette()
{
CRGB purple = CHSV( HUE_PURPLE, 255, 255);
CRGB green  = CHSV( HUE_GREEN, 255, 255);
CRGB black  = CRGB::Black;
currentPalette = CRGBPalette16(
green,  green,  black,  black,
purple, purple, black,  black,
green,  green,  black,  black,
purple, purple, black,  black );
}
const TProgmemPalette16 myRedWhiteBluePalette_p PROGMEM =
{
CRGB::Red,
CRGB::Gray,
CRGB::Blue,
CRGB::Black,

CRGB::Red,
CRGB::Gray,
CRGB::Blue,
CRGB::Black,

CRGB::Red,
CRGB::Red,
CRGB::Gray,
CRGB::Gray,
CRGB::Blue,
CRGB::Blue,
CRGB::Black,
CRGB::Black
};
```

　さて、なんか安物買いの初期不良っぽく盛り上がってきたなw

---

> オリジナル投稿：<br>
> NeoPixel 的なLEDモジュールを買う -2-｜kinneko｜pixivFANBOX<br>
> <https://kinneko.fanbox.cc/posts/5017205>
