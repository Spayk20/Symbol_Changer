WW = {'Å': 'A', 'Ä': 'A', 'å': 'a', 'ä': 'a', 'ã': 'a', 'á': 'a', 'à': 'a', 'â': 'a', 'ă': 'a', 'ą': 'a', 'ā': 'a',
          'Ö': 'O', 'Ø': 'O', 'ö': 'o', 'ø': 'o', 'ó': 'o', 'ô': 'o', 'è': 'e', 'ė': 'e', 'ë': 'e', 'é': 'e', 'ê': 'e',
          'É': 'E', 'í': 'i', 'î': 'i', 'ï': 'i', 'Ü': 'U', 'ü': 'u', 'ł': 'l', 'ñ': 'n', 'š': 's', 'Ş': 'S', 'ş': 's',
          'ß': 'ss', 'Ç': 'C', 'ç': 'c', 'ć': 'c', 'ğ': 'g', 'ž': 'z', 'Æ': 'AE', 'æ': 'ae', '—': '-', '®': ''}

DACH = {'Å': 'A', 'Ä': 'Ae', 'å': 'a', 'ä': 'ae', 'ã': 'a', 'á': 'a', 'à': 'a', 'â': 'a', 'ă': 'a', 'ą': 'a',
          'ā': 'a', 'Ö': 'Oe', 'Ø': 'O', 'ö': 'oe', 'ø': 'o', 'ó': 'o', 'ô': 'o', 'è': 'e', 'ė': 'e', 'ë': 'ee',
          'é': 'e', 'ê': 'e', 'É': 'E', 'í': 'i', 'î': 'i', 'ï': 'i', 'Ü': 'Ue', 'ü': 'ue', 'ł': 'l', 'ñ': 'n',
          'š': 's', 'Ş': 'S', 'ş': 's', 'ß': 'ss', 'Ç': 'C', 'ç': 'c', 'ć': 'c', 'ğ': 'g', 'ž': 'z', 'Æ': 'AE',
          'æ': 'ae', '—': '-', '®': ''}


def de_to_ascii(cell_val, region):
    count = 0
    for ch, val in region.items():
        if ch in cell_val:
            cell_val = cell_val.replace(ch, val)
            count += 1
    return cell_val, count
