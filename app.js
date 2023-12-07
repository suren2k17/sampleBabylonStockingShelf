window.addEventListener('DOMContentLoaded', function() {
    var canvas = document.getElementById('renderCanvas');
    var engine = new BABYLON.Engine(canvas, true);

    

    var createScene = function() {
        var scene = new BABYLON.Scene(engine);

        // Parameters: name, alpha, beta, radius, target, scene
        var camera = new BABYLON.ArcRotateCamera("camera1", Math.PI / 4, Math.PI / 3, 30, new BABYLON.Vector3(0, 5, 0), scene);
        camera.attachControl(canvas, true);

        var light = new BABYLON.HemisphericLight("light1", new BABYLON.Vector3(0, 1, 0), scene);
        var advancedTexture = BABYLON.GUI.AdvancedDynamicTexture.CreateFullscreenUI("UI");

        function createLabelForBox(text, box, boxWidth, boxHeight) {
            var label = new BABYLON.GUI.Rectangle("label for " + box.name);
            label.background = "black";
            label.height = "14px"; // Relative height of the label to the box
            label.width = (boxWidth * 10) + "px"; // Relative width of the label to the box
            label.color = "white";
            label.cornerRadius = 5;
            label.thickness = 0;
            label.verticalAlignment = BABYLON.GUI.Control.VERTICAL_ALIGNMENT_TOP;

            var text1 = new BABYLON.GUI.TextBlock();
            text1.text = text;
            text1.color = "white";
            text1.fontSize =  "12px"; // Relative font size to the label
            label.addControl(text1);

            advancedTexture.addControl(label);
            label.linkWithMesh(box); // Attach the label to the box
            label.linkOffsetY = -boxHeight * 1.5; // Move the label up above the box
        }
        

        // Function to create a random color material
        function getRandomColorMaterial(scene) {
            var material = new BABYLON.StandardMaterial("material", scene);
            material.diffuseColor = new BABYLON.Color3(Math.random(), Math.random(), Math.random());
            return material;
        }

        // Variables for shelf dimensions
        var shelfHeight = 0.3;
        var shelfWidth = 7;
        var shelfDepth = 2;
        var shelfSpacing = 3; // Space between shelves
        var totalShelves = 5;
        var boxSize = 1.3; // Size of the boxes
        var boxWidth = 1.3;
        var boxHeight = 1.3;
        var boxDepth = 1.3;

        // Calculate total height of the shelves
        var totalHeight = shelfHeight + (totalShelves - 1) * shelfSpacing;

        // Create shelves and cookie boxes
        for (let i = 0; i < totalShelves; i++) {
            var shelf = BABYLON.MeshBuilder.CreateBox("shelf" + i, {height: shelfHeight, width: shelfWidth, depth: shelfDepth}, scene);
            shelf.position.y = i * shelfSpacing;

             // Starting X position for the first box
             var startX = -(shelfWidth / 2) + (boxWidth / 2);

            // Create cookie boxes
            for (let j = 0; j < 5; j++) {
                var box = BABYLON.MeshBuilder.CreateBox("box" + i + "_" + j, {width: boxWidth, height: boxHeight, depth: boxDepth}, scene);
                box.material = getRandomColorMaterial(scene);
                box.position.x = startX + j * (boxWidth + 0.1);
                box.position.y = i * shelfSpacing + boxHeight / 2;
                box.position.z = 0;

                // Add label to the box
                createLabelForBox(String.fromCharCode(65 + i), box, boxWidth, boxHeight);
            }
        }

        // Create vertical beams with adjusted height
        var beamHeight = totalHeight + shelfHeight; // Slightly taller than total height of shelves
        var leftBeam = BABYLON.MeshBuilder.CreateBox("leftBeam", {height: beamHeight, width: 0.3, depth: shelfDepth}, scene);
        leftBeam.position.x = -shelfWidth / 2 - 0.15;
        leftBeam.position.y = beamHeight / 2 - shelfHeight / 2;

        var rightBeam = BABYLON.MeshBuilder.CreateBox("rightBeam", {height: beamHeight, width: 0.3, depth: shelfDepth}, scene);
        rightBeam.position.x = shelfWidth / 2 + 0.15;
        rightBeam.position.y = beamHeight / 2 - shelfHeight / 2;

        return scene;
    };

    var scene = createScene();

    // Run the render loop
    engine.runRenderLoop(function() {
        scene.render();
    });

    // Resize the engine when the window is resized
    window.addEventListener('resize', function() {
        engine.resize();
    });
});