class MetadataBuilder:

    @staticmethod
    def build(document):

        return {
            "source": document.metadata.get(
                "file_name"
            )
        }