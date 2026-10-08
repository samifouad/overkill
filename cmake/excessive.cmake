# fs_game defaults to excessive, so every executable needs the mod in its
# filesystem search path, including a macOS app copied out of the DMG.
add_custom_target(excessive_assets ALL)

foreach(TARGET IN ITEMS ${CLIENT_BINARY} ${SERVER_BINARY})
    if(NOT TARGET ${TARGET})
        continue()
    endif()

    add_custom_command(TARGET excessive_assets POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_directory
            "${CMAKE_SOURCE_DIR}/excessive"
            "$<TARGET_FILE_DIR:${TARGET}>/excessive"
        VERBATIM)
    add_dependencies(${TARGET} excessive_assets)
endforeach()

if(APPLE AND BUILD_CLIENT AND BUILD_MACOS_APP)
    install(DIRECTORY "${CMAKE_SOURCE_DIR}/excessive/"
        DESTINATION "${CLIENT_BINARY}.app/Contents/MacOS/excessive")
endif()

if(BUILD_SERVER OR (BUILD_CLIENT AND NOT (APPLE AND BUILD_MACOS_APP)))
    install(DIRECTORY "${CMAKE_SOURCE_DIR}/excessive/"
        DESTINATION excessive)
endif()
