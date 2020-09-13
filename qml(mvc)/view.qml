import QtQuick 2.12
import QtQuick.Window 2.12

Window {
  visible: true
  width: 640
  height: 480
    //color: "tomato"

  Rectangle {
    anchors.centerIn: parent
    height: 100
    width: parent.width / 2
    border {
      width: 1
      color: "black"
    }

    Component.onCompleted: {
      //console.log(view.contentHeight);
      //console.log(view.contentWidth);
      height = view.contentHeight;
      //width = view.contentWidth;
    }

    ListView {
      id: view
      anchors.fill: parent
      spacing: 2
      clip: true
      model: myModel

      delegate:
        Rectangle {
          height: 50
          width: view.width
          color: model.color
          radius: model.borderRadius

          Text {
            anchors.centerIn: parent
            text: model.text
          }
        }
    }
  }

// Text {
//     anchors.centerIn: parent
//     text: "Hello World"
// }
}