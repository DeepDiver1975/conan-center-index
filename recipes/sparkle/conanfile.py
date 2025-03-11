from conan import ConanFile
from conan.tools.apple import XcodeBuild
from conan.tools.files import get

class sparkleRecipe(ConanFile):
    name = "sparkle"
    version = "2.7.0"
    package_type = "library"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of sparkle package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def source(self):
        get(self, "https://github.com/sparkle-project/Sparkle/archive/refs/tags/2.7.0.tar.gz",
                  strip_root=True)

    def build(self):
        xcodebuild = XcodeBuild(self)
        xcodebuild.build("Sparkle.xcodeproj", "build")
