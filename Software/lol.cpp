#include <iostream>
#include <string>
#include <regex>
#include <vector>

int main() {
    int numOfInputs;
    std::cin >> numOfInputs;

    std::vector<std::string> array;

    for (int i = 0; i < numOfInputs; ++i) {
        int lenOfTestCase;
        std::cin >> lenOfTestCase;
        std::string testCase;
        std::cin >> testCase;
        array.push_back(testCase);
    }

   for (const auto& string : array) {
        std::regex pattern("A(.+?)?B(.+?)?C(.+?)?D(.+?)?E(.+?)?F(.+?)?G(.+?)?H(.+?)?I(.+?)?J(.+?)?K(.+?)?L(.+?)?M(.+?)?N(.+?)?O(.+?)?P(.+?)?Q(.+?)?R(.+?)?S(.+?)?T(.+?)?U(.+?)?V(.+?)?W(.+?)?X(.+?)?Y(.+?)?Z");
        std::smatch match;
        if (std::regex_search(string, match, pattern)) {
            std::string matchedSubstring = match.str(); // Extract the matched substring
            std::cout << matchedSubstring.size() << std::endl;
        } 
    }

    return 0;
}
