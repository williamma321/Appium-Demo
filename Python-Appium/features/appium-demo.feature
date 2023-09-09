Feature: iPhone About Me Mobile App test

  Scenario Outline: Navigate the App and Tag all icons
     Given the App loaded on devices
     When tab around the App <icon>
     Then display specific Tab <dispinfo>

    Examples:
       |      icon      |           dispinfo                |
       |  My Story      |        My Story Title             |
       |  Favorites     |         Favorites Title           |
       |  Fun Facts     |         Fun Facts Title           |