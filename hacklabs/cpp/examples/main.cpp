
#include "Lliurex.hpp"
#include <string>

int main(int argc, char * argv[])
{
	int * array = NULL;
	MAX_LENGTH=2048;
	
	array = new int[MAX_LENGTH];
	
	net::Lliurex::Lliurex * lx;
	
	lx = new net::Lliurex::Lliurex();
	lx.test();
	lx.sum(3,2);
	
	delete lx;
	
	delete array;
	
	return 0;
	
}
