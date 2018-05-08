#include <boost/filesystem.hpp>
#include <iostream>

namespace fs = ::boost::filesystem;
using namespace std;

int main()
{
	// get list of all image files
	vector<fs::path> filenames;
	std::string ext = ".png";
	fs::path root{"/home/nuc4/test_dataset/images/"};
  fs::recursive_directory_iterator it(root);
  fs::recursive_directory_iterator endit;
  
  while(it != endit)
  {
      if(fs::is_regular_file(*it) && it->path().extension() == ext)
      	  filenames.push_back(it->path().filename());
      ++it;
  }

    std::cout << "filenames size = " << filenames.size() << std::endl;

}
