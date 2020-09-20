import QtQuick 2.12
//import QtQuick.Window 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12

Item {
    //visible: true
    //color: "tomato"
    width: 120

    Rectangle {
        anchors.fill: parent
        border.width: 1
        border.color: "black"

        ListView {
            id: listView
            anchors.margins: 5
            anchors.top: parent.top
            anchors.left: parent.left
            anchors.right: parent.right
            height: parent.height / 2
            spacing: 2
            //focus: true
            clip: true

            highlight: Rectangle {
                //width: parent.width
                //height: 20
                color: "pink"
                radius: 2
            }
            highlightFollowsCurrentItem: true


            model: mySceneModel

            delegate: Rectangle {
                width: listView.width
                height: 20
                color: "transparent"

                Text {
                    //anchors.centerIn: parent
                    text: model.display
                }

                MouseArea {
                    anchors.fill: parent
                    onPressed: {
                        listView.currentIndex = model.index;
                    }
                }
            }
        }

        ColumnLayout {
            id: btnLayout
            anchors.bottom: parent.bottom
            anchors.left: parent.left
            anchors.right: parent.right
            height: parent.height / 2
            anchors.margins: 5
            spacing: 10

            Button {
                id: btnAddCircle
                Layout.alignment: Qt.AlignCenter
                //Layout.fillWidth: true
                //Layout.preferredWidth: parent.width - parent.anchors * 4
                text: "Добавить\nкруг"

                onClicked: {
                    mySceneWidget.addItem("Circle")
                }
            }
            Button {
                id: btnAddRect
                Layout.alignment: Qt.AlignCenter
                width: parent.width
                text: "Добавить\nквадрат"

                onClicked: {
                    mySceneWidget.addItem("Rectangle")
                }
            }
            Button {
                id: btnTriangle
                Layout.alignment: Qt.AlignCenter
                width: parent.width
                text: "Добавить\nтреугольник"
            }
        }
    }
}
