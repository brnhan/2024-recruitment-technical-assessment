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
    # create a list of all parent ids
    parents = {file.parent for file in files if file.parent != -1}

    # copy all ids and take intersection to get leaf ids
    possibleLeafs = {file.id for file in files}
    leafFilesSet = possibleLeafs.difference(parents)

    # create dictionary with all leaf ids and corresp names, then extract leaf file names
    fileDict = {file.id: file.name for file in files}
    leafFiles = [fileDict[id] for id in leafFilesSet]
    return leafFiles


"""
Task 2
"""
def kLargestCategories(files: list[File], k: int) -> list[str]:
    categoryDict = dict()

    # tally up all file category instances
    for file in files:
        for category in file.categories:
            categoryDict[category] = categoryDict.get(category, 0) + 1

    # sort by descending first touple (i.e, descending category file number), then if equivalence by zeroeth touple (i.e. name alphabetically)
    sortedCategories = sorted(categoryDict.items(), key=lambda x: (-x[1], x[0]))

    # return up until k categories
    return [category[0] for category in sortedCategories][0:k]


"""
Task 3
"""
def largestFileSize(files: list[File]) -> int:
    if not files: return 0
    filesDict = {file.id: file for file in files}

    fileSizeDict = dict()
    for file in files:
        # first add current file size to its dictionary entry
        fileSizeDict[file.id] = fileSizeDict.get(file.id, 0) + file.size

        # recursively add current file size to all parents
        if file.parent != -1: updateParentsSize(filesDict, filesDict[file.parent], fileSizeDict, file.size)

    return max(fileSizeDict.values())


def updateParentsSize(filesDict: dict[int, File], parent: File, fileSizeDict: dict[int, int], childFileSize: int):
    fileSizeDict[parent.id] = fileSizeDict.get(parent.id, 0) + childFileSize

    if parent.parent == -1: return
    updateParentsSize(filesDict, filesDict[parent.parent], fileSizeDict, childFileSize)



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
