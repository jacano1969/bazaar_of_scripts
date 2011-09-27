
#include "Lliurex.hpp"
#include <iostream>

using namespace std;

namespace net
{
	namespace Lliurex
	{

		Lliurex::Lliurex()
		{
			cout << "Constructor"<<endl;
		}

		Lliurex::~Lliurex()
		{
			cout << "Destructor " <<endl;
		}

		void Lliurex::test()
		{
			cout << "test de void" <<endl;
		}

		int Lliurex::sum(int a, int b)
		{
			cout << "suma " << (a+b) <<endl;
		}
	}			
}
