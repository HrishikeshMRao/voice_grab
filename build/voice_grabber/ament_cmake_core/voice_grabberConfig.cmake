# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_voice_grabber_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED voice_grabber_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(voice_grabber_FOUND FALSE)
  elseif(NOT voice_grabber_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(voice_grabber_FOUND FALSE)
  endif()
  return()
endif()
set(_voice_grabber_CONFIG_INCLUDED TRUE)

# output package information
if(NOT voice_grabber_FIND_QUIETLY)
  message(STATUS "Found voice_grabber: 0.0.0 (${voice_grabber_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'voice_grabber' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${voice_grabber_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(voice_grabber_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${voice_grabber_DIR}/${_extra}")
endforeach()
