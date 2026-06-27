param(
  [Parameter(Mandatory=$true)][string]$Pdf,
  [string]$OutPrefix = "page",
  [int]$Width = 850
)

Add-Type -AssemblyName System.Runtime.WindowsRuntime | Out-Null

# Generic Await for IAsyncOperation<T>
$asTaskGeneric = ([System.WindowsRuntimeSystemExtensions].GetMethods() |
  Where-Object { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and
    $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0]
function AwaitOp($op, $resultType) {
  $task = $asTaskGeneric.MakeGenericMethod($resultType).Invoke($null, @($op))
  $task.Wait(-1) | Out-Null
  $task.Result
}
# Await for IAsyncAction (no result)
$asTaskAction = ([System.WindowsRuntimeSystemExtensions].GetMethods() |
  Where-Object { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and
    $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncAction' })[0]
function AwaitAct($action) {
  $task = $asTaskAction.Invoke($null, @($action))
  $task.Wait(-1) | Out-Null
}

[Windows.Data.Pdf.PdfDocument,         Windows.Data.Pdf,        ContentType=WindowsRuntime] | Out-Null
[Windows.Storage.StorageFile,          Windows.Storage,         ContentType=WindowsRuntime] | Out-Null
[Windows.Storage.Streams.InMemoryRandomAccessStream, Windows.Storage.Streams, ContentType=WindowsRuntime] | Out-Null
[Windows.Data.Pdf.PdfPageRenderOptions,Windows.Data.Pdf,        ContentType=WindowsRuntime] | Out-Null

$full = (Resolve-Path $Pdf).Path
$file = AwaitOp ([Windows.Storage.StorageFile]::GetFileFromPathAsync($full)) ([Windows.Storage.StorageFile])
$doc  = AwaitOp ([Windows.Data.Pdf.PdfDocument]::LoadFromFileAsync($file)) ([Windows.Data.Pdf.PdfDocument])

"Pages: $($doc.PageCount)"
for ($i = 0; $i -lt $doc.PageCount; $i++) {
  $page = $doc.GetPage($i)
  $stream = [Windows.Storage.Streams.InMemoryRandomAccessStream]::new()
  $opts = [Windows.Data.Pdf.PdfPageRenderOptions]::new()
  $opts.DestinationWidth = [uint32]$Width
  AwaitAct ($page.RenderToStreamAsync($stream, $opts))

  $size = [uint32]$stream.Size
  $reader = [Windows.Storage.Streams.DataReader]::new($stream.GetInputStreamAt(0))
  AwaitOp ($reader.LoadAsync($size)) ([uint32]) | Out-Null
  $bytes = New-Object byte[] $size
  $reader.ReadBytes($bytes)
  $out = "{0}-{1:D2}.png" -f $OutPrefix, ($i+1)
  [System.IO.File]::WriteAllBytes((Join-Path (Get-Location) $out), $bytes)
  "wrote $out"
  $page.Dispose()
}
