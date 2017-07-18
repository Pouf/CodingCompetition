def largest_histogram(histogram):
    result, width = 0, len(histogram) + 1

    for i in range(1, width):
        for j in range(width - i):
            rect = i * min(histogram[j:][:i])
            result = max(result, rect)

    return result
