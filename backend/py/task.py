from dataclasses import dataclass

@dataclass
class File:
    id: int
    name: str
    categories: list[str]
    parent: int
    size: int


"""
Task 1
"""
def leafFiles(files: list[File]) -> list[str]:
    parents = {file.parent for file in files if file.parent != -1}
    possibleLeafs = {file.id for file in files}
    leafFilesSet = possibleLeafs.difference(parents)

    fileDict = {file.id: file.name for file in files}
    leafFiles = [fileDict[id] for id in leafFilesSet]
    return leafFiles


"""
Task 2
"""
def kLargestCategories(files: list[File], k: int) -> list[str]:
    categoryDict = dict()
    for file in files:
        for category in file.categories:
            # if category in categoryDict:
            #     categoryDict[category] += 1
            # else:
            #     categoryDict[category] = 1
            categoryDict[category] = categoryDict.get(category, 0) + 1

    sortedCategories = sorted(categoryDict.items(), key=lambda x: (-x[1], x[0]))

    return [category[0] for category in sortedCategories][0:k]


"""
Task 3
"""
def largestFileSize(files: list[File]) -> int:
    if not files: return 0
    filesDict = {file.id: file for file in files}

    fileSizeDict = dict()
    for file in files:
        updateFileAndParentsSize(filesDict, file, fileSizeDict)

    return max(fileSizeDict.values())


def updateFileAndParentsSize(filesDict: dict[int, File], file: File, fileSizeDict: dict[int, int]):
    fileSizeDict[file.id] = fileSizeDict.get(file.id, 0) + file.size

    if file.parent == -1: return
    updateFileAndParentsSize(filesDict, filesDict[file.parent], fileSizeDict)



if __name__ == '__main__':
    testFiles = [
        File(1, "Document.txt", ["Documents"], 3, 1024),
        File(2, "Image.jpg", ["Media", "Photos"], 34, 2048),
        File(3, "Folder", ["Folder"], -1, 0),
        File(5, "Spreadsheet.xlsx", ["Documents", "Excel"], 3, 4096),
        File(8, "Backup.zip", ["Backup"], 233, 8192),
        File(13, "Presentation.pptx", ["Documents", "Presentation"], 3, 3072),
        File(21, "Video.mp4", ["Media", "Videos"], 34, 6144),
        File(34, "Folder2", ["Folder"], 3, 0),
        File(55, "Code.py", ["Programming"], -1, 1536),
        File(89, "Audio.mp3", ["Media", "Audio"], 34, 2560),
        File(144, "Spreadsheet2.xlsx", ["Documents", "Excel"], 3, 2048),
        File(233, "Folder3", ["Folder"], -1, 4096),
    ]

    assert sorted(leafFiles(testFiles)) == [
        "Audio.mp3",
        "Backup.zip",
        "Code.py",
        "Document.txt",
        "Image.jpg",
        "Presentation.pptx",
        "Spreadsheet.xlsx",
        "Spreadsheet2.xlsx",
        "Video.mp4"
    ]

    assert kLargestCategories(testFiles, 3) == [
        "Documents", "Folder", "Media"
    ]

    assert largestFileSize(testFiles) == 20992
