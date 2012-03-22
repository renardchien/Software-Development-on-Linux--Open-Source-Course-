#include "SDL/SDL.h"
#include "SDL/SDL_image.h"	
#include <string>	

// ================== Declare global variables =======================
// ===================================================================
SDL_Surface* background_image = NULL;	// placed here so that any function can access them

// this contains the FULL set of frames for our sprite even though we only display one of them
SDL_Surface* Sprite = NULL;
// our poiter to the screen surface
SDL_Surface* screen = NULL;

// display rectangles for sprite
SDL_Rect background_position;
SDL_Rect Sprite_position;
SDL_Rect source;

// set screen dimensions
const int SCREEN_WIDTH = 800;
const int SCREEN_HEIGHT = 600;
const int SCREEN_BPP = 32;



// ================== Functions ======================================
// ===================================================================

SDL_Surface *Load_image( std::string filename )
{
	SDL_Surface* loaded_image = NULL;
	SDL_Surface* compatible_image = NULL;

	if(filename.c_str() == NULL) { // check to see if a filename was provided
		// if not exit the function
		return NULL;
	}

	// load the image using our new IMG_Load function from sdl-Image1.2
	loaded_image = IMG_Load( filename.c_str() );

	if( loaded_image == NULL ){ // check to see if it loaded properly
		// if not exit the function
		return NULL;
	}	

	// the image loaded fine so we can now convert it to the current display depth
	compatible_image = SDL_DisplayFormat( loaded_image );

	if( compatible_image != NULL ) {
		// specify a colour that will be used to signify 'transparent' pixels
		Uint32 colorkey = SDL_MapRGB( compatible_image->format, 0, 0, 0); // choose black
		// now tell SDL to remeber our choice
		SDL_SetColorKey( compatible_image, SDL_RLEACCEL | SDL_SRCCOLORKEY, colorkey);
		// SDL_RLEACCEL is run lenght encoding acceleration to speed up the colorkeying
		// SDL_SRCCOLORKEY tells SDL that this color key applies to the source image
	}

	// Destroy the old copy
	SDL_FreeSurface( loaded_image );

	// return a pointer to the newly created display compatible image
	return compatible_image;
}

bool Init()
{
	background_position.x = 0; 			// initialize position rectangle
	background_position.y = 0;

	Sprite_position.x = 350;
	Sprite_position.y = 200;
	source.x = 0;
	source.y = 0;
	source.w = 50; // because we arent going to display the full picture
	source.h = 140; // were just going to display the top left corner

	//Initialize SDL video subsystems
    	if( SDL_Init( SDL_INIT_VIDEO ) == -1 )    {
		return false;    
	}
	// create screen 800x600x32bpp in software rendering mode.
	screen = SDL_SetVideoMode( SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_BPP, SDL_SWSURFACE ); 
	
	background_image = Load_image("background.jpg"); // load our background Surface
	if( background_image == NULL ){ 
		printf("unable to load Background Image\n");
		return false;
	}

	Sprite = Load_image("sprite.bmp"); // load our sprite images on a surface
	if( Sprite == NULL ){
		printf("unable to load Sprite Images\n");
		return false;
	}
	return true;
	
}

void shutdown(void)
{
	// Destroy image surface
	SDL_FreeSurface( background_image );	
	SDL_FreeSurface( Sprite );	
	SDL_Quit();
	
}	

// ====================== main ===========================================
// =======================================================================

int main( int argc, char* argv[] )
{
	if(Init() == false) {
		// use SDL_Error() to tell us what went wrong
		printf("Unable to Intialise Program error is: %s\n\n", SDL_GetError() ); 
	}
	// make sure SDL shuts down in the event of a crash
	atexit( shutdown );

	// put the image on the screen surface
	SDL_BlitSurface( background_image, NULL, screen, &background_position ); // put the background on
	// now place the sprite over the top
	SDL_BlitSurface( Sprite, &source, screen, &Sprite_position ); 	
	// now change the position back to 0,0 for the background
	
	
	SDL_Flip( screen ); // send the screen surface to be displayed

	//Wait 7 seconds
	SDL_Delay( 4000 );	

	printf("Completed SDL"); 

	return 0; // program completed successfully
}
