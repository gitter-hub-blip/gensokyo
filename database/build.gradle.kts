/*
 * This file was generated by the Gradle 'init' task.
 *
 * This project uses @Incubating APIs which are subject to change.
 */



//CONFIGURATION IN DATABASE
plugins {
    id("buildlogic.java-library-conventions")
}


repositories {
    mavenCentral()
    google()        // backup download Google Maven
    maven { url = uri("https://jitpack.io") }
}


dependencies {
    implementation(project(":network"))
    implementation("org.xerial:sqlite-jdbc:3.45.3.0")
}
