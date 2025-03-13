from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import get, copy

class qtkeychainRecipe(ConanFile):
    name = "qtkeychain"
    version = "0.15.0"
    package_type = "library"

    # Optional metadata
    license = "BSD-3-Clause"
    url = "https://github.com/frankosterfeld/qtkeychain"
    description = "Platform-independent Qt API for storing passwords securely."
    topics = ("qt", "keychain")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def source(self):
        get(self, "https://github.com/frankosterfeld/qtkeychain/archive/refs/tags/0.15.0.zip", strip_root=True)

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires("qt/6.7.3", options={"with_dbus": True}, transitive_headers=True, transitive_libs=True)
        self.requires("dbus/1.15.8", transitive_headers=True, transitive_libs=True)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["BUILD_WITH_QT6"] = True
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["qtkeychain"]

