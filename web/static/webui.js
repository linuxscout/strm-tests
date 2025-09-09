

function updateArgsForm() {
    const command = document.getElementById("selectcommand").value;
    const argsDiv = document.getElementById("argsForm");
    const exampleDiv = document.getElementById("exampleDiv");
    argsDiv.innerHTML = ""; // clear old fields

    if (command === "random") return;

    const cmdInfo = commandsInfo[command];
    if (!cmdInfo || !cmdInfo.args) return;

    for (const [argName, argMeta] of Object.entries(cmdInfo.args)) {
        // Label
        const label = document.createElement("label");
        label.textContent = argMeta.label + ": ";
        label.setAttribute("for", argName);
        label.className = "block text-sm font-medium mb-1";

        let input;

        // Input types
        switch (argMeta.type) {
            case "string":
                input = document.createElement("input");
                input.type = "text";
                input.value = argMeta.default || "";
                input.className =
                    "w-full border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500";
                break;

            case "integer":
                input = document.createElement("input");
                input.type = "number";
                input.value = argMeta.default || 0;
                if (argMeta.range) {
                    input.min = argMeta.range[0];
                    input.max = argMeta.range[1];
                }
                input.className =
                    "w-full border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500";
                break;

            case "float":
                input = document.createElement("input");
                input.type = "number";
                input.value = argMeta.default || 0.0;
                input.step="0.01"
//                if (argMeta.range) {
//                    input.min = argMeta.range[0];
//                    input.max = argMeta.range[1];
//                }
                input.className =
                    "w-full border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500";
                break;


            case "boolean":
                input = document.createElement("input");
                input.type = "checkbox";
                input.checked = argMeta.default || false;
                input.className =
                    "rounded border-gray-300 text-blue-600 focus:ring-blue-500";
                break;

            case "list":
                input = document.createElement("textarea");
                input.rows = 2;
                input.value = JSON.stringify(argMeta.default || []);
//                input.placeholder = JSON.stringify(argMeta.default || []);
                input.className =
                    "w-full border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500";
                break;

            case "dict":
                input = document.createElement("textarea");
                input.rows = 3;
                input.placeholder = JSON.stringify(argMeta.default || {});
                input.className =
                    "w-full border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500";
                break;

            default:
                input = document.createElement("input");
                input.type = "text";
                input.value = argMeta.default || "";
                input.className =
                    "w-full border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500";
        }

        input.name = "args[" + argName + "]";

        // Handle choices (dropdown)
        if (argMeta.choices) {
            const select = document.createElement("select");
            select.name = "args[" + argName + "]";
            select.className =
                "w-full border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500";

            argMeta.choices.forEach(choice => {
                const opt = document.createElement("option");
                opt.value = choice;
                opt.text = choice;
                if (choice === argMeta.default) opt.selected = true;
                select.appendChild(opt);
            });
            input = select;
        }

        // Wrap field
        const div = document.createElement("div");
        div.className = "mb-4";
        div.appendChild(label);
        div.appendChild(input);
        argsDiv.appendChild(div);
    }

    // Show example if available
    if (cmdInfo.example) {
        exampleDiv.innerHTML =
            `<h4 class="font-semibold mb-2">Example Question:</h4><pre class="bg-gray-100 p-2 rounded">${cmdInfo.example}</pre>`;
    } else {
        exampleDiv.innerHTML =
            `<h4 class="font-semibold mb-2">Example Question:</h4><pre class="bg-gray-100 p-2 rounded">Not available</pre>`;
    }
}
        function updateCommands() {
            const category = document.getElementById("selectcategory").value;
            const commandSelect = document.getElementById("selectcommand");

            // Clear existing options
            commandSelect.innerHTML = "";

            // Add default "random" option
            const optRandom = document.createElement("option");
            optRandom.value = "random";
            optRandom.text = "Random Question";
            commandSelect.appendChild(optRandom);

            // Get commands for the chosen category
            let cmds = [];
            if (category === "random") {
                // merge all commands from all categories
                for (const c in categoryCommands) {
                    cmds = cmds.concat(categoryCommands[c]);
                }
            } else {
                cmds = categoryCommands[category] || [];
            }

            // Add options
            cmds.forEach(cmd => {
                const opt = document.createElement("option");
                opt.value = cmd.name;
                opt.text = cmd.short;
                commandSelect.appendChild(opt);
            });
        }

        // Initialize on load
        window.onload = function() {
            updateCommands();
            document.getElementById("selectcommand").addEventListener("change", updateArgsForm);
        };


function resetForm() {
    // reset selects
    document.getElementById("selectcategory").value = "random";
    document.getElementById("selectformat").value = "html";
    document.getElementById("selectquiz").value = "random";
    document.getElementById("random").checked = false;

    // re-update commands dropdown + args
    updateCommands();
    document.getElementById("selectcommand").value = "random";
    updateArgsForm();

    // clear result div
    document.getElementById("resultDiv").innerHTML =
        '<pre id="resultPre">Result will appear here...</pre>';
}

      //(update preview live)
function updatePreview() {
  const command = document.getElementById("selectcommand").value;
  const args = {};
  document.querySelectorAll("#argsForm input, #argsForm select, #argsForm textarea").forEach(el => {
    if (!el.name) return;
    let key = el.name.replace(/^args\[|\]$/g, "");
    args[key] = el.type === "checkbox" ? el.checked : el.value;
  });

  // simple preview text
  let html = `<p><b>Command:</b> ${command}</p>`;
  html += `<pre>${JSON.stringify(args, null, 2)}</pre>`;

  document.getElementById("previewPanel").innerHTML = html;
}

// hook into form changes
document.addEventListener("input", updatePreview);
document.addEventListener("change", updatePreview);

                // display a hint fro current command
document.getElementById("selectcommand").addEventListener("change", function() {
  const value = this.value;
  document.getElementById("commandHint").textContent = commandsInfo[value].long || value;
});
        /* submit function */
        document.addEventListener("DOMContentLoaded", function () {
        const form= document.getElementById("quizForm").addEventListener("submit", async function (e) {
      e.preventDefault(); // prevent normal form submission

    // show spinner, clear result
        document.getElementById("spinner").style.display = "block";
        document.getElementById("resultDiv").innerHTML =
          '<pre id="resultPre">Generating...</pre>';

      const category = document.getElementById("selectcategory").value;
      const command = document.getElementById("selectcommand").value;
      const outformat = document.getElementById("selectformat").value;
      const quizid = document.getElementById("selectquiz").value;
      const select_random_values = document.getElementById("random").checked;


      // Collect args from the dynamically generated argsForm
        const args = {[command]:{}};
        const inputs = document.querySelectorAll("#argsForm input, #argsForm select, #argsForm textarea");
        inputs.forEach(el => {
          if (!el.name || !el.name.startsWith("args[")) return;
            // clean key
            let key = el.name;
            key = key.slice(5, -1); // strip args[...] wrapper
            let value = ""
          if (el.type === "checkbox") {
             value = el.checked;
          } else if (el.type === "radio") {
            if (el.checked)
               value= el.value;
          } else {
            value = el.value;
          }
            args[command][key] = value;
        });
      const payload = {
        category: category,
        command: command,
        select_random_values:select_random_values,
        outformat:outformat,
        quizid:quizid,
        args: args
  };
//            console.log("payload", payload);



    try {
      const response = await fetch("/submit", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
      });


        const result = await response.text();
        document.getElementById("resultDiv").innerHTML = result;
        console.log("Server response:", result);
        }
                catch (err) {
      document.getElementById("resultDiv").innerHTML =
        `<pre>Error: ${err.message}</pre>`;
    } finally {
      // hide spinner
      document.getElementById("spinner").style.display = "none";
    }
//const result = await response.json();
//console.log("Server response:", result);
//      // (optional) display the result in the page
//
//      alert(JSON.stringify(result, null, 2));
    });
    });