$(document).ready(function () {
  let my_dropzone = $("#dropzone");
  my_dropzone.dropzone({
    url: "/api/image/flip/",
    init: function () {
      this.on("success", (initial_file, response) => {
        let base_64_rotated_file = response.file;
        let base_64_prefix = initial_file.dataURL.split(",")[0];
        let previewElement = $(initial_file.previewElement);
        let processed_img_tag = previewElement.find(
          "img[data-dz-processed-thumbnail]"
        );
        processed_img_tag.attr(
          "src",
          `${base_64_prefix},${base_64_rotated_file}`
        );
      });
      this.on("error", (file, message) => {
        this.removeFile(file)
        alert(message.file)
      });
    },
    previewTemplate: `
      <div class="dz-preview dz-file-preview">
        <div class="dz-size" data-dz-size></div>
        <img data-dz-thumbnail />
        <img data-dz-processed-thumbnail />
      </div>
    `,
    thumbnailWidth: null,
    thumbnailHeight: null,
  });
});
